import wolframalpha
import wikipedia
import wx


class MyFrame(wx.Frame):  # The GUI for the App
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(500, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                                wx.CLOSE_BOX | wx.CLIP_CHILDREN, title="Pydex")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Hello its Pydex! How can i help you?")
        sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(500, 40))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        self.Show()

    def OnEnter(self, event):  # User interaction
        user_input = self.txt.GetValue()
        user_input = user_input.lower()
        try:  # Based on Wolfram Alpha
            app_id = "E7H2EU-267UWJ7XRP"
            client = wolframalpha.Client(app_id)
            result = client.query(user_input)
            answer = next(result.results).text
            print(answer)
        except:  # Based on Wikipedia
            # wikipedia.set_lang("") - If you want to change language
            user_input.split(' ')
            # In case the user enter a question word like "What" "Where is" and so on...
            user_input = " ".join(input[2:])
            print(wikipedia.summary(user_input, sentences=2))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
