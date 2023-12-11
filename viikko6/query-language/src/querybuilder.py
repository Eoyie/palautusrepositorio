from matchers import And, PlaysIn, HasAtLeast, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, old_queries = All(), queries = All(), or_test = False):
        self._queries = old_queries
        
        if or_test:
            self._queries = Or(self._queries, queries)
        else:
            self._queries = And(self._queries, queries)
                
    def build(self):
        return self._queries
    
    def playsIn(self, team):
        return QueryBuilder(self._queries, PlaysIn(team))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._queries, HasFewerThan(value, attr))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._queries, HasAtLeast(value, attr))
    
    def oneOf(self, *terms):
        return QueryBuilder(terms[0], terms[1], True)