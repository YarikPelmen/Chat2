import customtkinter
import PIL
from modules.find_path import find_path


class App(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.PC_WIDTH_SCREEN = self.winfo_screenwidth()
        self.PC_HEIGHT_SCREEN = self.winfo_screenheight()
        #self.FIND_PATH = find_path
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_WIDTH_SCREEN}+{0}")
        self.title("Chat")

        

        self.resizable(False, False)


        self.IMAGE = customtkinter.CTkImage(
           dark_image= PIL.Image.open(find_path(name_file="images/image.jpeg")),
           size= (self.APP_WIDTH, self.APP_HEIGHT)
        )

        self.IMAGE_LABEL = customtkinter.CTkLabel(master = self, text = "моя перша практична робота з customtkinter", image = self.IMAGE)
        self.IMAGE_LABEL.grid(row = 10, column = 10)

