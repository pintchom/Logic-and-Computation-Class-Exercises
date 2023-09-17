from tabulate import tabulate

class Formula(object):
    pass

class Value(Formula):
    def __init__(self,value):
        self.value=value
    def __repr__(self):
        return "Value(" + repr(self.value) + ")"
    def variables(self):
        return set()
    def evaluate(self,values):
        return self.value
    
class Variable(Formula):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "Variable(" + repr(self.name) + ")"
    def variables(self):
        return {self.name}
    def evaluate(self,values):
        return values[self.name];
    
class And(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "And(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return self.first.evaluate(values) and self.second.evaluate(values)

class Or(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Or(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return self.first.evaluate(values) or self.second.evaluate(values)

class Implies(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Implies(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return (not self.first.evaluate(values)) or self.second.evaluate(values)

class Not(Formula):
    def __init__(self,sub):
        self.sub=sub
    def __repr__(self):
        return "Not(" + repr(self.sub) + ")"
    def variables(self):
        return self.sub.variables()
    def evaluate(self,values):
        return not self.sub.variables()

class Iff(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Iff(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return (self.first.evaluate(values) and self.second.evaluate(values)) or ((not self.first.evaluate(values)) and (not self.second.evaluate(values)))
        

# listAllPossibleValues takes a list of variable names, it returns a list of pairs,
#   giving all possible combinations of True/False values for the given variables
#   Each list can be converted to a dictionary by passing it to dict(),
#   and then passed to the evaluate() method defined above.

def listAllPossibleValues(varlist):
    if varlist==[]:
        return [[]]
    else:
        firstvar, restvars = varlist[0], varlist[1:]
        restValues = listAllPossibleValues(restvars)
        prependTrue = [ [(firstvar,True)] + r for r in restValues]
        prependFalse = [ [(firstvar,False)] + r for r in restValues]
        return prependTrue + prependFalse

def truthValues(formula):
    return [ formula.evaluate(dict(vals))
             for vals in listAllPossibleValues(list(formula.variables())) ]

# truthTable(formula) returns the truth table of the provided formula

def truthTable(formula):
    variableList=list(formula.variables())
    variableList.sort()
    headers = variableList+[str(formula)]
    rows = [ [v[1] for v in vals] + [formula.evaluate(dict(vals))]
             for vals in listAllPossibleValues(variableList) ]
    return tabulate(rows, headers=headers)

# DEMO – this should work once you add the missing code above

myformula=And(Implies(Variable('p'),Variable('q')),
                  Implies(Variable('p'),Variable('r')))

print( truthTable(myformula) )

# Uncomment the following lines and provide the code to compute them

def isTautology(formula):
    values = truthValues(formula)
    if False in values:
        return False
    return True

def isSatisfiable(formula):
    values = truthValues(formula)
    if True in values:
        return True
    return False
        
def isContradiction(formula):
    values = truthValues(formula)
    if True in values:
        return False
    return True

print(isTautology(myformula))
print(isSatisfiable(myformula))
print(isContradiction(myformula))
