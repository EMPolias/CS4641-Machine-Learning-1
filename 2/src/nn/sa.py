def simmulated_annealing(model, iterNum):
	curr_accu = model.evaluate(None)
	accu_list.push(curr_accu)

	for i in range(iterNum):
		model.annealing_vary_para()
		curr_accu = model.evaluate(curr_accu) # pass in current accuracy for comparing and update para
		accu_list.push(curr_accu)

	return accu_list