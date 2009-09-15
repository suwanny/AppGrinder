package net.grinder.console.appbenchui;

import com.facebook.thrift.protocol.TBinaryProtocol;
import com.facebook.thrift.protocol.TBinaryProtocol.Factory;
import com.facebook.thrift.server.TServer;
import com.facebook.thrift.server.TThreadPoolServer;
import com.facebook.thrift.transport.TServerSocket;
import com.facebook.thrift.transport.TTransportException;

import net.grinder.common.GrinderBuild;
import net.grinder.common.Logger;
import net.grinder.console.model.SampleModel;

public class AppBenchThriftServer extends Thread {
	private final int PORT = 7070;
	private final Logger m_logger;
	private final SampleModel m_sampleModel;
	private TServer server; 
	private AppBenchConsoleImpl m_thriftImpl = null; 
	private String m_lastReport = ""; 
  private AppBenchUI m_ui; 
	
	public AppBenchThriftServer(AppBenchUI ui, SampleModel sampleModel, Logger logger) {
    m_ui = ui;
		m_logger = logger;
	    m_logger.output(GrinderBuild.getName());
	    m_sampleModel = sampleModel;
		m_logger.output("Create AppBenchConsole ThriftServer");
	}
	
	@Override
    public void run() {
		m_logger.output("Starting grinder Console thrift server on port " + PORT + ".");
		// thrift server start 
		try {
			TServerSocket serverTransport = new TServerSocket(PORT);
			m_thriftImpl = new AppBenchConsoleImpl(m_ui, m_sampleModel, m_logger); 
			AppBenchConsole.Processor processor = new AppBenchConsole.Processor(m_thriftImpl); // Implementation
			Factory protFactory = new TBinaryProtocol.Factory(true, true);
			server = new TThreadPoolServer(processor, serverTransport, protFactory);
			m_logger.output("Starting server on port " + PORT );
			server.serve();
		} catch (TTransportException e) {
			e.printStackTrace();
		}
	}
	
	public void shutdown() {
		m_logger.output("Shutting down grinder Console thrift server on port " + PORT + ".");
		// thrift server stop 
		server.stop(); 
	}
	
	public synchronized void setReport(String report) {
		m_lastReport = report; 
		if(m_thriftImpl != null)
			m_thriftImpl.setReport(report); 
	}
}
