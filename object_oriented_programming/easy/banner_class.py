from textwrap import wrap

class Banner:
    def __init__(self, message, width=None):
        self.message = message
        self.width = width

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        if self.width is None:
            return f"| {' ' * len(self.message)} |"
        return f"| {' ' * (self.width - 4)} |"

    def _horizontal_rule(self):
        if self.width is None:
            return f"+-{'-' * len(self.message)}-+"
        return f"+-{'-' * (self.width - 4)}-+"
        
    def _message_line(self):
        if self.width is None:
            return f"| {self.message} |"
        message_list = wrap(self.message, self.width - 4)
        lines_list = [f"| {message_line.center(self.width -4)} |" 
                      for message_line in message_list]
        return '\n'.join(lines_list)
    
# Comments show expected output

banner = Banner('To boldly go where no one has gone before.', 15)
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+