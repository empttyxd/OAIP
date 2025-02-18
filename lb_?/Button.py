class button:
    def __init__(self):
        self.status = 'Unclicked'

    def click(self):
        if self.status == 'Unclicked':
            self.status = 'Clicked'
    def function(self):
        if self.status == 'Clicked':
            print('did you think something would happen here? its just a button')
        else:
            print('Press this button!')