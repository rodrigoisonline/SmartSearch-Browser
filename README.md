<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartSearch Browser Overview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            overflow: hidden;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #ccc 3px solid;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 2em;
        }
        .main-content {
            margin-top: 20px;
        }
        .section {
            margin-bottom: 20px;
        }
        h2 {
            background: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            margin: 10px 0;
            padding: 10px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .advantages, .names {
            display: flex;
            flex-wrap: wrap;
        }
        .advantages div, .names div {
            flex: 1;
            min-width: 200px;
            margin: 10px;
            padding: 20px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>SmartSearch Browser Overview</h1>
        </div>
    </header>
    <div class="container">
        <div class="main-content">
            <section class="section">
                <h2>Key Components</h2>
                <ul>
                    <li><strong>BrowserFrame Class:</strong> Defines the main window of the browser application.</li>
                    <li><strong>CreateControls Method:</strong> Creates various UI elements like buttons and a URL bar.</li>
                    <li><strong>DoLayout Method:</strong> Arranges the UI elements using sizers to ensure proper layout.</li>
                    <li><strong>BindEvents Method:</strong> Binds UI elements (buttons, URL bar) to their respective event handlers.</li>
                    <li><strong>Event Handlers:</strong>
                        <ul>
                            <li>OnEnterUrl: Loads a URL entered by the user.</li>
                            <li>OnPageLoad: Updates URL bar and status when a page loads.</li>
                            <li>OnNavigating, OnError: Update status bar during navigation and on errors.</li>
                            <li>Navigation Buttons (OnBack, OnForward, OnReload, etc.): Control browser navigation.</li>
                            <li>OnBookmark: Adds the current page to bookmarks.</li>
                            <li>OnDuckSearch, OnGoogleSearch: Performs searches on DuckDuckGo and Google.</li>
                            <li>ScanPage: Analyzes the page URL and searches for specific terms.</li>
                            <li>SearchDuckDuckGo, SearchGoogle: Parses search terms from DuckDuckGo and Google URLs.</li>
                            <li>ScanForLyftURLs: Scans the page for URLs related to Lyft.</li>
                        </ul>
                    </li>
                    <li><strong>BrowserApp Class:</strong> Initializes and starts the application, displaying the main browser window.</li>
                </ul>
            </section>
            <section class="section">
                <h2>Advantages</h2>
                <div class="advantages">
                    <div>User Interface: Provides a user-friendly interface with buttons for common browser functions and a text box for URL input.</div>
                    <div>Navigation Controls: Includes back, forward, reload, home, and stop buttons, improving user experience.</div>
                    <div>Bookmarking: Allows users to bookmark pages for easy access later.</div>
                    <div>Custom Searches: Facilitates quick searches on DuckDuckGo and Google with predefined queries.</div>
                    <div>Page Scanning: Automatically scans pages for specific URLs related to Lyft.</div>
                </div>
            </section>
            <section class="section">
                <h2>Cool Name Suggestions</h2>
                <div class="names">
                    <div>"LyftBrowser" – Emphasizes the focus on Lyft-related searches and URLs.</div>
                    <div>"QuickSearch Navigator" – Highlights the search capabilities and navigation features.</div>
                    <div>"WebExplorer" – A general name that reflects the web browsing and exploration features.</div>
                    <div>"SmartSearch Browser" – Emphasizes the intelligent search and scanning functionalities.</div>
                    <div>"Bookmark Navigator" – Focuses on the bookmarking and navigation aspects of the browser.</div>
                </div>
            </section>
        </div>
    </div>
</body>
</html>