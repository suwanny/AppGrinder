package net.grinder.console.appbenchui;

import java.util.Arrays;
import java.util.Comparator;

import net.grinder.common.GrinderBuild;
import net.grinder.common.Logger;
import net.grinder.common.processidentity.AgentProcessReport;
import net.grinder.common.processidentity.ProcessReport;
import net.grinder.common.processidentity.WorkerProcessReport;
import net.grinder.console.ConsoleFoundation.UI;
import net.grinder.console.common.ErrorHandler;
import net.grinder.console.common.ProcessReportDescriptionFactory;
import net.grinder.console.common.Resources;
import net.grinder.console.communication.ProcessControl;
import net.grinder.console.model.SampleModel;

import com.facebook.thrift.*;


public class AppBenchConsoleImpl implements AppBenchConsole.Iface {
	private final Logger m_logger;
	private final SampleModel m_sampleModel;
	private String m_lastReport = ""; 
  private AppBenchUI m_ui; 
	  
	public AppBenchConsoleImpl(AppBenchUI ui, SampleModel sampleModel, Logger logger) {
    m_ui = ui; 
		m_logger = logger;
	  m_logger.output(GrinderBuild.getName());
	  m_sampleModel = sampleModel;
	}
	
	public synchronized void setReport(String report) {
		m_lastReport = report; 
	}
	
	@Override
	public void start(String arg1, String arg2) throws TException {
		m_logger.output("grinder command - start"); 
    //m_sampleModel.start();
    m_ui.OnStart(); 
	}

	@Override
    public void stop(String arg1, String arg2) throws TException {
		m_logger.output("grinder command - stop"); 
    //m_sampleModel.stop();
    m_ui.OnStop();
	}

	@Override
    public String get_status(String arg1, String arg2) throws TException {
		//return "grinder command - get_status";
		return m_lastReport; 
	}
}
