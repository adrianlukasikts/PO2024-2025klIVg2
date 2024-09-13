class Field:
    def __init__(self, piece=None):
        self.piece = piece

    def get_piece_name(self):
        if not self.piece:
            return "____"
        return str(self.piece)
