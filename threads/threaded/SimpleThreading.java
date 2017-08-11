package threaded;

/**
 * Simples exemplo de uso de multiplas threads
 * em java, com o uso de execucao paralela
 * otimizando assim o tempo de execucao.
 *
 * @author Gabriel Fernandes
 */
public class SimpleThreading implements Runnable {
	static double totalTime;
	static final int coreNumber = Runtime.getRuntime().availableProcessors();
	static int coreFactor =  coreNumber <= 4 ? 4/coreNumber : 1;

	/**
	 * Verificador de numero primo.
	 * 
	 * @param num	numero na qual deseja-se verificar se eh primo
	 * @return		true caso num seja primo, false caso contrario
	 */
    static boolean prime(int num) {
        if(num < 2) 
            return false;
        if(num == 2)
            return true;
        if(num%2 == 0)
            return false;

        for(int i = 3; i<(num/2); i += 2) {
            if(num%i == 0)
                return false;
        }
        
        return true;
    }
    
    /**
     * Gera o n-esimo numero primo.
     * 
     * @param target	n-esimo desejado
     * @return			o n-esimo primo
     */
    static int yieldprime(int target) {
        int count = 1;
        int primes = 2;
        while(true) {
            if(count == target)
                return primes;
            primes += 1;
            if(prime(primes))
                count++;
        }
    }
    
    /**
     * Realiza a entrega de uma atividade para a thread
     * que a chamar, contando tambem o tempo de execucao
     * que essa thread faz a atividade (calcular numeros primos).
     * 
     * @param message	mensagem para imprimir antes dos resultados
     */
    static void releaseTask(String message) {
		long start = System.currentTimeMillis();
		int primo = yieldprime(20000);
		System.out.println(message);
		System.out.print("O 20,000 n-esimo primo: ");
		System.out.println(primo);
		double end = (System.currentTimeMillis() - start)/1000.0;
		totalTime += end;
		System.out.print("tempo levado para essa thread calcular(em segs): ");
		System.out.println(end);
		System.out.println();
	}
	
	@Override
	public void run() {
		releaseTask("Hello i'm a thread");
	}

	public static void main(String[] args) throws InterruptedException {
		// inicio do timer global
		long init = System.currentTimeMillis();
		
		// criacao das threads
		Thread t = new Thread(new SimpleThreading());
		Thread t2 = new Thread(new Runnable() {
			@Override
			public void run() {
				releaseTask("Hello i'm another thread");
			}
		});
		Thread t3 = new Thread(new SimpleThreading());

		System.out.println("Iniciando execucao...");
		System.out.println();
		
		// iniciar a execucao das threads
		t.start();
		t2.start();
		t3.start();

		// uso da main thread para tambem participar do "thread pool"
		releaseTask("I'm the main thread");

		// aguardar todas terminarem
		t.join();
		t2.join();
		t3.join();

		// dados finais sobre a execucao
		double finish = (System.currentTimeMillis() - init)/1000.0;
		System.out.print("Seu pc levou ");
		System.out.print(finish);
		System.out.println(" segs para calcular o 20,000 n-esimo primo 4 vezes");
		System.out.print("Teria levado ");
		System.out.print(totalTime/coreFactor);
		System.out.println(" segs para calcular se nao tivessemos usando ");
		System.out.print(coreNumber <= 4 ? coreNumber : 4);
		System.out.println(" cores do seu processador para rodar "
				+ "threads em paralelo");
	}
}