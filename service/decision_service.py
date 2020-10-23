class DecisionService:

    LOAN_AMOUNT_THRESHOLD = 400

    def __A1(self, loan_amount:int) -> str:
        if loan_amount <= self.LOAN_AMOUNT_THRESHOLD:
            return 'accept'

    def __A2(self, loan_amount:int) -> str:
        return 'performing A2 logic'



    
    
    def get_decision(self, bv_category:str):
        if bv_category == 'A1':
            return self.__A1(300)
        elif bv_category == 'A2':
            return self.__A2()
        elif bv_category == 'A3':
            return self.__A3()
        else:
            return self.__D1()