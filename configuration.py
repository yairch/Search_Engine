from os import getcwd

class ConfigClass:
    def __init__(self):
        self.corpusPath = getcwd()
        self.savedFileMainFolder = "\\postings"
        self.saveFilesWithStem = self.savedFileMainFolder + "\\WithStem"
        self.saveFilesWithoutStem = self.savedFileMainFolder + "\\WithoutStem"
        self.toStem = False

        print('Project was created successfully..')

    def get__corpusPath(self):
        return self.corpusPath
