import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;

import javax.swing.JFrame;

public class Main extends Canvas implements Runnable{
	
	private static final long serialVersionUID = 1L;
	private static Thread thread;
	public static JFrame frame;
	private static boolean isRunning;
	public BufferedImage image; 
	public void Window() {
		frame = new JFrame("Jogo");
		frame.add(this);
		frame.setResizable(false);
		frame.pack();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLayout(new FlowLayout());
		frame.setLocationRelativeTo(null);
		frame.pack();
		frame.setVisible(true);
	}
	public Main() {
		this.setPreferredSize(new Dimension(640,480));
		Window();
		image = new BufferedImage(160,120,BufferedImage.TYPE_INT_RGB);
	}
	public static void main(String args[]) {
		System.out.println("hello world");
		Main main = new Main();
		main.start();
	}
	public synchronized void start() {
		thread = new Thread(this);
		isRunning = true;
		thread.start();
	}
	public synchronized void stop() {
		
	}
	public void tick() {
		
	}
	public void render() {
		System.out.println("g");
		BufferStrategy bs = this.getBufferStrategy();
		if(bs == null) {
			this.createBufferStrategy(3);
			return;
		}
		Graphics g = bs.getDrawGraphics();
		g.setColor(new Color(19,19,19));
		g.fillRect(0, 0, 640, 480);
		g.setColor(new Color(189,219,143));
		g = bs.getDrawGraphics();
		g.drawImage(image, 0, 0, 640, 480,null);
		bs.show();
	}
	public void run() {
		long lastTime = System.nanoTime();
		double AmountOfTicks = 60.0;
		double ns = 1000000000/AmountOfTicks;
		double delta = 0;
		int frames = 0;
		double times = System.currentTimeMillis();
		while(isRunning) {
			long now = System.nanoTime();
			delta+= (now - lastTime) / ns;
			lastTime = now;
			if(delta >=1) {
				tick();
				render();
				frames++;
				delta--;
			}
			if(System.currentTimeMillis() - times >= 1000) {
				System.out.println("FPS"+frames);
				frames = 0;
				times+=1000;
			}
		}
		
	}
}
