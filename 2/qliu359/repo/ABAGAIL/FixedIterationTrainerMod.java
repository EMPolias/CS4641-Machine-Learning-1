// package shared;
import shared.Trainer;
import java.io.*;

public class FixedIterationTrainerMod {
    private Trainer trainer;
    private int iterations;
    private int recStep;
    private String outFile;

    public FixedIterationTrainerMod(Trainer t, int iter, int step, String file) {
        trainer = t;
        iterations = iter;
        recStep = step;
        outFile = file;
    }

    public double train(double start) {
        double sum = 0;
        double end = 0;
        double trainingTime = 0;
        PrintWriter pw;
        try {
            FileWriter fw = new FileWriter(outFile, true); // Append to the file
            BufferedWriter bw = new BufferedWriter(fw);
            pw = new PrintWriter(bw);
            pw.println("Start");

            for (int i = 0; i < iterations; i++) {
                double fitness = trainer.train();
                if (i % recStep == 0) {
                    end = System.nanoTime();
                    trainingTime = end - start;
                    trainingTime = end - start;
                    trainingTime /= Math.pow(10,9);
                    System.out.println(i + "," + String.format("%.2f", fitness) + "," + String.format("%.2f", trainingTime));
                    pw.println(i + "," + String.format("%.2f", fitness)+ "," + String.format("%.2f", trainingTime));
                }
                sum += fitness;
            }
            pw.println("End Time: " + String.format("%.3f", trainingTime));
            pw.flush();
            pw.close();

        } catch(Exception E) {
            System.out.println("Opening the file not success");
        }

        return sum / iterations;
    }


}
