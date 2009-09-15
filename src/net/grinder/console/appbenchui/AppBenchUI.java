
package net.grinder.console.appbenchui;

import java.util.Arrays;
import java.util.Comparator;

import net.grinder.common.GrinderBuild;
import net.grinder.common.Logger;
import net.grinder.common.processidentity.AgentProcessReport;
import net.grinder.common.processidentity.ProcessReport;
import net.grinder.common.processidentity.WorkerProcessReport;
import net.grinder.console.ConsoleFoundation;
//import net.grinder.console.ConsoleFoundation.UI;
import net.grinder.console.common.ErrorHandler;
import net.grinder.console.common.ProcessReportDescriptionFactory;
import net.grinder.console.common.Resources;
import net.grinder.console.communication.ProcessControl;
import net.grinder.console.model.ConsoleProperties;
import net.grinder.console.model.SampleModel;
import net.grinder.console.model.SampleModelViews;
import net.grinder.console.distribution.FileDistribution;


public class AppBenchUI implements ConsoleFoundation.UI {
  private final Resources m_resources;
  private final ConsoleProperties m_properties;
  private final SampleModelViews m_sampleModelViews;
  private final ProcessControl m_processControl;
  private final FileDistribution m_fileDistribution;

  private final Logger m_logger;
  private final ErrorHandler m_errorHandler;
  private final Thread m_shutdownHook;
  private final SampleModel m_sampleModel;
  private final AppBenchThriftServer m_thrift; // suwanny 

  /**
   * Constructor.
   *
   * @param resources Console resources.
   * @param processControl Console process control.
   * @param sampleModel Console sample model.
   * @param logger Logger.
   */
  public AppBenchUI(Resources resources,
          ConsoleProperties consoleProperties,
          SampleModel model,
          SampleModelViews sampleModelViews,
          ProcessControl processControl,
          FileDistribution fileDistribution,
          Logger logger) {

    m_resources = resources;
    m_properties = consoleProperties;
    m_sampleModelViews = sampleModelViews;
    m_processControl = processControl;
    m_fileDistribution = fileDistribution;

    m_logger = logger;
    m_logger.output(GrinderBuild.getName());

    m_shutdownHook = new Thread(new ShutdownHook(resources));
    Runtime.getRuntime().addShutdownHook(m_shutdownHook);

    m_errorHandler = new ErrorHandlerImplementation();

    processControl.addProcessStatusListener(new ProcessListener(resources));

    m_sampleModel = model;
    m_sampleModel.addModelListener(
      new SampleModel.AbstractListener() {
        public void stateChanged() {
          m_logger.output(m_sampleModel.getState().getDescription());
        }
      });

    // add thrift server - suwanny (2009.08.17)
    m_thrift = new AppBenchThriftServer(this, m_sampleModel, m_logger); 
    m_thrift.start(); 

  }

  public void OnStart() {
    m_logger.output("call start..");  
    //m_sampleModel.start();
    m_sampleModel.stop();
    m_processControl.startWorkerProcesses(null);
  }

  public void OnStop() {
    m_logger.output("call stop..");
    m_sampleModel.stop();
    m_processControl.stopAgentAndWorkerProcesses(); 
  }

  /**
   * For unit tests.
   *
   * @return The shutdown hook.
   */
  Thread getShutdownHook() {
    return m_shutdownHook;
  }

  /**
   * Return our error handler.
   *
   * @return The error handler.
   */
  public ErrorHandler getErrorHandler() {
    return m_errorHandler;
  }

  private final class ProcessListener implements ProcessControl.Listener {
    private final Comparator m_processReportComparator =
      new ProcessReport.StateThenNameThenNumberComparator();

    private final Comparator m_processReportsComparator =
      new ProcessControl.ProcessReportsComparator();

    private final ProcessReportDescriptionFactory m_descriptionFactory;

    private final String m_noConnectedAgents;
    private String m_lastReport = null;

    public ProcessListener(Resources resources) {
      m_descriptionFactory = new ProcessReportDescriptionFactory(resources);
      m_noConnectedAgents = resources.getString("noConnectedAgents.text");
    }

    public void update(ProcessControl.ProcessReports[] processReports) {

      final String reportString;

      if (processReports.length == 0) {
        reportString = m_noConnectedAgents;
      }
      else {
        final StringBuffer report =
          new StringBuffer(processReports.length * 128);

        Arrays.sort(processReports, m_processReportsComparator);

        for (int i = 0; i < processReports.length; ++i) {
          if (i > 0) {
            report.append(", ");
          }

          final AgentProcessReport agentProcessStatus =
            processReports[i].getAgentProcessReport();
          report.append(
            m_descriptionFactory.create(agentProcessStatus).toString());

          final WorkerProcessReport[] workerProcessStatuses =
            processReports[i].getWorkerProcessReports();

          if (workerProcessStatuses.length > 0) {
            report.append(" { ");

            Arrays.sort(workerProcessStatuses, m_processReportComparator);

            for (int j = 0; j < workerProcessStatuses.length; ++j) {
              if (j > 0) {
                report.append(", ");
              }

              report.append(
                m_descriptionFactory.create(
                  workerProcessStatuses[j]).toString());
            }

            report.append(" }");
          }
        }

        reportString = report.toString();
      }

      if (!reportString.equals(m_lastReport)) {
        m_logger.output(reportString);
        m_lastReport = reportString;
        m_thrift.setReport(m_lastReport);
      }
    }
  }

  private final class ErrorHandlerImplementation implements ErrorHandler {
    public void handleErrorMessage(String errorMessage) {
      m_logger.error(errorMessage);
    }

    public void handleErrorMessage(String errorMessage, String title) {
      m_logger.error("[" + title + "] " + errorMessage);
    }

    public void handleException(Throwable throwable) {
      m_logger.error(throwable.getMessage());
      throwable.printStackTrace(m_logger.getErrorLogWriter());
      m_logger.getErrorLogWriter().flush();
    }

    public void handleException(Throwable throwable, String title) {
      m_logger.error(title);
      throwable.printStackTrace(m_logger.getErrorLogWriter());
      m_logger.getErrorLogWriter().flush();
    }

    public void handleInformationMessage(String informationMessage) {
      m_logger.output(informationMessage);
    }
  }

  private final class ShutdownHook implements Runnable {
    private final String m_shutdownMessage;
    private boolean m_stopped = false;

    public ShutdownHook(Resources resources) {
      m_shutdownMessage = resources.getString("finished.text");
    }

    public synchronized void run() {
      if (!m_stopped) {
        m_stopped = true;
        m_logger.output(m_shutdownMessage);
      }
    }
  }
}
