
#filter object, used to filter out protocol fields
class messageType:

    #New session object as defined within the srs and sdd
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def editName(self,newName):
        #name cannot be blank
        if newName == "" or newName == " ":
            print "name cannot be blank"

        self.name = newName
        #print "name succesfully changed"

    def editExpressoin(self,newExpression):
        self.expression = newExpression
