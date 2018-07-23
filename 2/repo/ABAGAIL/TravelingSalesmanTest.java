import java.util.Arrays;
import java.util.Random;
import java.io.*;
import dist.DiscreteDependencyTree;
import dist.DiscretePermutationDistribution;
import dist.DiscreteUniformDistribution;
import dist.Distribution;

import opt.SwapNeighbor;
import opt.GenericHillClimbingProblem;
import opt.HillClimbingProblem;
import opt.NeighborFunction;
import opt.RandomizedHillClimbing;
import opt.SimulatedAnnealing;
import opt.example.*;
import opt.ga.CrossoverFunction;
import opt.ga.SwapMutation;
import opt.ga.GenericGeneticAlgorithmProblem;
import opt.ga.GeneticAlgorithmProblem;
import opt.ga.MutationFunction;
import opt.ga.StandardGeneticAlgorithm;
import opt.prob.GenericProbabilisticOptimizationProblem;
import opt.prob.MIMIC;
import opt.prob.ProbabilisticOptimizationProblem;
// import shared.FixedIterationTrainer;

public class TravelingSalesmanTest {
    /** The n value */
    private static final int N = 50;
    private static final int IterNum = 5000;
    private static final int recStep = 50;
    private static final String outFile = "TravelingSalesman.txt";

    public static void main(String[] args) {
        Random random = new Random();
        // create the random points
        double[][] points = new double[N][2];
        for (int i = 0; i < points.length; i++) {
            points[i][0] = random.nextDouble();
            points[i][1] = random.nextDouble();
        }
        // for rhc, sa, and ga we use a permutation based encoding
        TravelingSalesmanEvaluationFunction ef = new TravelingSalesmanRouteEvaluationFunction(points);
        Distribution odd = new DiscretePermutationDistribution(N);
        NeighborFunction nf = new SwapNeighbor();
        MutationFunction mf = new SwapMutation();
        CrossoverFunction cf = new TravelingSalesmanCrossOver(ef);
        HillClimbingProblem hcp = new GenericHillClimbingProblem(ef, odd, nf);
        GeneticAlgorithmProblem gap = new GenericGeneticAlgorithmProblem(ef, odd, mf, cf);

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

        SimulatedAnnealing sa = new SimulatedAnnealing(1E12, .95, hcp);
        fit = new FixedIterationTrainerMod(sa, IterNum, recStep, outFile);
        start = System.nanoTime();
        fit.train(start);
        end = System.nanoTime();
        trainingTime = end - start;
        trainingTime /= Math.pow(10,9);

        System.out.println("SA: " + ef.value(sa.getOptimal()) + " Time: " + trainingTime);

        System.out.println("GA Starts");

        StandardGeneticAlgorithm ga = new StandardGeneticAlgorithm(200, 150, 20, gap);
        fit = new FixedIterationTrainerMod(ga, IterNum, recStep, outFile);
        start = System.nanoTime();
        fit.train(start);
        end = System.nanoTime();
        trainingTime = end - start;
        trainingTime /= Math.pow(10,9);

        System.out.println("GA: " + ef.value(ga.getOptimal()) + " Time: " + trainingTime);

        System.out.println("MIMIC Starts");

        // for mimic we use a sort encoding
        ef = new TravelingSalesmanSortEvaluationFunction(points);
        int[] ranges = new int[N];
        Arrays.fill(ranges, N);
        odd = new  DiscreteUniformDistribution(ranges);
        Distribution df = new DiscreteDependencyTree(.1, ranges);
        ProbabilisticOptimizationProblem pop = new GenericProbabilisticOptimizationProblem(ef, odd, df);

        MIMIC mimic = new MIMIC(200, 100, pop);
        fit = new FixedIterationTrainerMod(mimic, IterNum, recStep, outFile);
        start = System.nanoTime();
        fit.train(start);
        end = System.nanoTime();
        trainingTime = end - start;
        trainingTime /= Math.pow(10,9);

        System.out.println("MIMIC: " + ef.value(mimic.getOptimal()) + " Time: " + trainingTime);

    }
}
