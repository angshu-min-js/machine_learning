def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    
    ### your code goes here!
    from sklearn import linear_model
    clf = linear_model.Ridge (alpha = .5)
    reg = clf.fit(ages_train, net_worths_train)
    
    
    return reg