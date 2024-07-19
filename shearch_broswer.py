import wx
import wx.html2
import urllib.parse
import requests
from bs4 import BeautifulSoup #beautifulsoup4

class BrowserFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(BrowserFrame, self).__init__(*args, **kw)
        self.browser = wx.html2.WebView.New(self)
        self.browser.LoadURL("http://www.duckduckgo.com")
        self.bookmarks = {
            "Duck Bonus Lyft": "http://www.duckduckgo.com?q=something=",
            "Google Bonus Lyft": "http://www.google.com/search?q=something="
        }

        self.SetTransparent(240)  # Adjust the transparency level as desired
        self.CreateControls()
        self.DoLayout()
        self.BindEvents()

    def CreateControls(self):
        self.url_bar = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.go_btn = wx.Button(self, label="Go")
        self.bookmark_btn = wx.Button(self, label="Bookmark")
        self.duck_search_btn = wx.Button(self, label="Search DuckDuckGo")
        self.google_search_btn = wx.Button(self, label="Search Google")
        self.back_btn = wx.Button(self, label="Back")
        self.forward_btn = wx.Button(self, label="Forward")
        self.reload_btn = wx.Button(self, label="Reload")
        self.home_btn = wx.Button(self, label="Home")
        self.stop_btn = wx.Button(self, label="Stop")
        self.status_bar = self.CreateStatusBar()
        self.home_url = "http://www.duckduckgo.com"

    def DoLayout(self):
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self.back_btn)
        btn_sizer.Add(self.forward_btn)
        btn_sizer.Add(self.reload_btn)
        btn_sizer.Add(self.home_btn)
        btn_sizer.Add(self.stop_btn)
        btn_sizer.Add(self.bookmark_btn)
        btn_sizer.Add(self.duck_search_btn)
        btn_sizer.Add(self.google_search_btn)
        url_sizer = wx.BoxSizer(wx.HORIZONTAL)
        url_sizer.Add(self.url_bar, 1, wx.EXPAND)
        url_sizer.Add(self.go_btn)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(url_sizer, 0, wx.EXPAND)
        sizer.Add(btn_sizer, 0, wx.EXPAND)
        sizer.Add(self.browser, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def BindEvents(self):
        self.url_bar.Bind(wx.EVT_TEXT_ENTER, self.OnEnterUrl)
        self.go_btn.Bind(wx.EVT_BUTTON, self.OnEnterUrl)
        self.bookmark_btn.Bind(wx.EVT_BUTTON, self.OnBookmark)
        self.duck_search_btn.Bind(wx.EVT_BUTTON, self.OnDuckSearch)
        self.google_search_btn.Bind(wx.EVT_BUTTON, self.OnGoogleSearch)
        self.back_btn.Bind(wx.EVT_BUTTON, self.OnBack)
        self.forward_btn.Bind(wx.EVT_BUTTON, self.OnForward)
        self.reload_btn.Bind(wx.EVT_BUTTON, self.OnReload)
        self.home_btn.Bind(wx.EVT_BUTTON, self.OnHome)
        self.stop_btn.Bind(wx.EVT_BUTTON, self.OnStop)
        self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.OnPageLoad, self.browser)
        self.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.OnNavigating, self.browser)
        self.Bind(wx.html2.EVT_WEBVIEW_ERROR, self.OnError, self.browser)

    def OnEnterUrl(self, event):
        url = self.url_bar.GetValue()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.LoadURL(url)

    def OnPageLoad(self, event):
        self.url_bar.SetValue(self.browser.GetCurrentURL())
        self.status_bar.SetStatusText("Page loaded")
        self.ScanPage()

    def OnNavigating(self, event):
        self.status_bar.SetStatusText("Loading...")

    def OnError(self, event):
        self.status_bar.SetStatusText(f"Error: {event.GetString()}")

    def OnBack(self, event):
        if self.browser.CanGoBack():
            self.browser.GoBack()

    def OnForward(self, event):
        if self.browser.CanGoForward():
            self.browser.GoForward()

    def OnReload(self, event):
        self.browser.Reload()

    def OnHome(self, event):
        self.browser.LoadURL(self.home_url)

    def OnStop(self, event):
        self.browser.Stop()
        self.status_bar.SetStatusText("Loading stopped")

    def OnBookmark(self, event):
        current_url = self.browser.GetCurrentURL()
        bookmark_name = f"Bookmark {len(self.bookmarks) + 1}"
        self.bookmarks[bookmark_name] = current_url
        print(f"Added bookmark: {bookmark_name} -> {current_url}")

    def OnDuckSearch(self, event):
        self.browser.LoadURL("http://www.duckduckgo.com?q=drive-with-lyft?ref=")

    def OnGoogleSearch(self, event):
        self.browser.LoadURL("http://www.google.com/search?q=drive-with-lyft?ref=")

    def ScanPage(self):
        current_url = self.browser.GetCurrentURL()
        if "duckduckgo" in current_url:
            self.SearchDuckDuckGo()
        elif "google" in current_url:
            self.SearchGoogle()

    def SearchDuckDuckGo(self):
        url = self.browser.GetCurrentURL()
        parsed_url = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed_url.query)
        if "q" in query:
            search_term = query["q"][0]
            if "drive-with-lyft?ref=" in search_term:
                self.ScanForLyftURLs()

    def SearchGoogle(self):
        url = self.browser.GetCurrentURL()
        parsed_url = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed_url.query)
        if "q" in query:
            search_term = query["q"][0]
            if "drive-with-lyft?ref=" in search_term:
                self.ScanForLyftURLs()

    def ScanForLyftURLs(self):
        current_url = self.browser.GetCurrentURL()
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        lyft_urls = []
        for link in links:
            href = link['href']
            if "drive-with-lyft?ref=" in href:
                lyft_urls.append(href)
        if lyft_urls:
            print("Found Lyft URLs:")
            for url in lyft_urls:
                print(url)
        else:
            print("No Lyft URLs found on this page.")

class BrowserApp(wx.App):
    def OnInit(self):
        frame = BrowserFrame(None, title="Enhanced Browser", size=(1000, 800))
        frame.Show()
        return True

if __name__ == "__main__":
    app = BrowserApp()
    app.MainLoop()
