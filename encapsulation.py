class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        print("pass")

    def _unsafe_method(self):
        print("nopass")

print(PublicPrivateExample._unsafe_method)