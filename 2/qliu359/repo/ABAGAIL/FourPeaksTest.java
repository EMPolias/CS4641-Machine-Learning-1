import java.util.Arrays;
import java.io.*;
import dist.DiscreteDependencyTree;
import dist.DiscreteUniformDistribution;
import dist.Distribution;

import opt.DiscreteChangeOneNeighbor;
import opt.EvaluationFunction;
import opt.GenericHillClimbingProblem;
import opt.HillClimbingProblem;
import opt.NeighborFunction;
import opt.RandomizedHillClimbing;
import opt.SimulatedAnnealing;
import opt.example.*;
import opt.ga.CrossoverFunction;
import opt.ga.DiscreteChangeOneMutation;
import opt.ga.SingleCrossOver;
import opt.ga.GenericGeneticAlgorithmProblem;
import opt.ga.GeneticAlgorithmProblem;
import opt.ga.MutationFunction;
import opt.ga.StandardGeneticAlgorithm;
import opt.prob.GenericProbabilisticOptimizationProblem;
import opt.prob.MIMIC;
import opt.prob.ProbabilisticOptimizationProblem;
// import FixedIterationTrainerMod;

public class FourPeaksTest {
    /** The n value */
    private static final int N = 200;
    /** The t value */
    private static final int T = N / 5;
    private static final int IterNum = 20000;
    private static final int recStep = IterNum/200;
    private static final String outFile = "FourPeaks.txt";

    public static void main(String[] args) {
        int[] ranges = new int[N];
        Arrays.fill(ranges, 2);
        EvaluationFunction ef = new FourPeaksEvaluationFunction(T);
        Distribution odd = new DiscreteUniformDistribution(ranges);
        NeighborFunction nf = new DiscreteChangeOneNeighbor(ranges);
        MutationFunction mf = new DiscreteChangeOneMutation(ranges);
        CrossoverFunction cf = new SingleCrossOver();
        Distribution df = new DiscreteDependencyTree(.1, ranges);
        HillClimbingProblem hcp = new GenericHillClimbingProblem(ef, odd, nf);
        GeneticAlgorithmProblem gap = new GenericGeneticAlgorithmProblem(ef, odd, mf, cf);
        ProbabilisticOptimizationProblem pop = new GenericProbabilisticOptimizationProblem(ef, odd, df);

        double start, trainingTime, end = 0;

        // Delete former records
        try {
            FileWriter fw = new FileWriter(outFile, false); // Append to the file
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw);
            pw.println("");
            pw.flush();
            pw.close();
        } catch(Exception E) {
            System.out.println("Deleting the file not success");
        }

        System.out.println("RHC Starts");

        RandomizedHillClimbing rhc = new RandomizedHillClimbing(hcp);
        FixedIterationTrainerMod fit = new FixedIterationTrainerMod(rhc, IterNum, recStep, outFile);
        start = System.nanoTime();
        fit.train(start);
        end = System.nanoTime();
        trainingTime = end - start;
        trainingTime /= Math.pow(10,9);

        System.out.println("RHC: " + ef.value(rhc.getOptimal()) + " Time: " + trainingTime);

        System.out.println("SA Starts");

        SimulatedAnnealing sa = new SimulatedAnnealing(1E11, .95, hcp);
        fit = new FixedIterationTrainerMod(sa, IterNum, recStep, outFile);
        start = System.nanoTime();
        fit.train(start);
        end = System.nanoTime();
        trainingTime = end - start;
        trainingTime = end - start;
        trainingTime /= Math.pow(10,9);

        System.out.println("SA: " + ef.value(sa.getOptimal()) + " Time: " + trainingTime);

        System.out.println("GA Starts");

        StandardGeneticAlgorithm ga = new StandardGeneticAlgorithm(200, 100, 10, gap);
        fit = new FixedIterationTrainerMod(ga, IterNum, recStep, outFile);
        start = System.nanoTime();
        fit.train(start);
        end = System.nanoTime();
        trainingTime = end - start;
        trainingTime = end - start;
        trainingTime /= Math.pow(10,9);

        System.out.println("GA: " + ef.value(ga.getOptimal()) + " Time: " + trainingTime);

        System.out.println("MIMIC Starts");

        MIMIC mimic = new MIMIC(200, 20, pop);
        fit = new FixedIterationTrainerMod(mimic, IterNum, recStep, outFile);
        start = System.nanoTime();
        fit.train(start);
        end = System.nanoTime();
        trainingTime = end - start;
        trainingTime = end - start;
        trainingTime /= Math.pow(10,9);

        System.out.println("MIMIC: " + ef.value(mimic.getOptimal()) + " Time: " + trainingTime);
    }
}
