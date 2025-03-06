class button:
    def __init__(self):
        self.status = 'Unclicked'
        self.color = 'Red'
        self.form = 'Rectangle'
        self.width = 5
        self.length = 10
        self.size = f'{self.length} x {self.width}'
        self.x = -2
        self.y = 1
        self.position = f'{self.x}:{self.y}'

    def change_position(self,x, y):
        self.x = x
        self.y = y

    def change_size(self, width, length):
        self.width = width
        self.length = length

    def change_color(self, color):
        self.color = color


    def click(self):
        if self.status == 'Unclicked':
            self.status = 'Clicked'

    def function(self):
        if self.status == 'Clicked':
            print('''⢘⠀⡂⢠⠆⠀⡰⠀⡀⢀⣠⣶⣦⣶⣶⣶⣶⣾⣿⣿⡿⢀⠈⢐⠈⠀⠀
⡃⠀⡀⣞⡇⢰⠃⣼⣇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣰⣻⡀⢸⠀⠀⠀
⢐⢀⠀⣛⣽⣇⠘⢸⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⠟⢡⣾⣿⢿⡇⠀⡃⠀⠀
⠀⠀⢐⠀⠀⢳⣿⡯⡞⣾⣿⣿⣿⣿⣿⣿⢿⣿⠟⢁⣴⣿⣿⣿⡜⢷⠀⢘⠄⠀
⠀⠀⠂⡂⠸⡆⠙⠛⡵⣿⣿⣿⣿⣿⡿⠤⠛⣠⣴⣿⣿⠿⣟⣟⠟⢿⡆⢳⠀⠀
⠀⠀⠸⠁⠀⡾⠁⠀⠀⠀⠀⠉⠉⠉⠈⣠⡌⢁⠄⡛⠡⠉⠍⠙⢳⢾⠁⢸⠀⠀
⠀⠀⢈⠀⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣷⡎⠙⢬⣳⣪⡯⢜⣷⢸⠂⡈⠄⠀
⠀⠀⠐⡀⠀⢣⠀⠀⠀⠀⠀⠀⠀⣴⣿⣾⣷⢿⢻⣅⣌⡯⢛⣿⣿⡞⠠⡁⠂⠀
⠀⠀⠀⠄⠀⢉⡀⠀⠀⢀⡠⠤⠼⣇⣳⣿⣿⣟⡜⣿⣿⣿⣿⣿⣿⡇⠸⠡⠀⠀
⠀⠀⡀⠅⠀⠃⢀⡀⣿⡹⠗⢀⠛⠥⣺⣿⣿⡝⢹⣸⣿⣿⣿⣿⡏⠠⠰⠈⠐⠀
⠠⠈⠀⠄⣀⠀⠀⠸⠻⠦⠀⠀⠀⠀⠀⠉⠐⠀⠘⠻⢹⣿⡿⠃⠀⡀⠕⣈⠡⡄
⠀⠀⣴⡀⣬⠁⠀⠀⡁⠂⠀⣀⣀⠔⠌⠤⣀⡀⠀⠀⡈⢸⠪⠀⠀⡌⠤⠈⡀⣠
⠀⠀⣿⣿⣾⡇⠀⠀⠀⣴⢫⣾⠃⠠⢰⣶⣴⠶⣿⣦⠀⠀⠀⢄⣂⠀⠀⠰⠀⠙
⠀⠀⠉⠛⠛⠀⢀⣴⣿⢗⡟⠡⣄⣀⡀⠀⢀⣤⠞⡅⠀⠁⠀⡾⠀⠀⠠⡗⠀⢀
⠀⠀⠀⠀⠀⣴⡿⢋⠔⠃⠀⠀⠍⠙⠉⠈⠑⠁⠂⠀⠀⠀⡡⡁⣠⡼⣸⠅⠀⠘
⠀⠀⠀⣼⠛⢡⠔⠁⠐⣆⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⡔⡞⢛⣿⡿⠃⠏⠀⠀⢠
⠀⠀⠀⠈⠗⠀⠀⠀⠀⠘⣷⣀⢀⣀⣀⠀⡀⢀⣌⡧⠂⠀⡞⠛⡟⠀⠀⠀⡠⠜
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠈⠙⠙⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⡂⠠⠤⢶''')
        else:
            print('Press this button!')
