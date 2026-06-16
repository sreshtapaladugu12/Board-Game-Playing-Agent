def bayes(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

def expected_utility(utility, probability):
    return utility * probability