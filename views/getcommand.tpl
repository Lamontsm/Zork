<!--This is the template called by /NextCommand -->
<html>
    <head>
        <title>Game Play</title>
        <link rel="stylesheet" type="text/css" href="/css/default.css">
    </head>
</html>
<body>
    <h1 id="header">Howdy!</h1>
    <h2>{{error}}</h2>
    <br></br>
    <p>{{text}}</p>
    <img class="bordered-image" src={{graphic}} />
    <br></br>
    <p>Your items are: {{inventory}}</p>
    <br></br>
    <p>(Your commands in this simple version are limited to go north, quit, or error)</p>
    <form action="/Command" method="post">
        What is your command? <input name="command" type="text" />
        <input value="Submit" type="submit" />
    </form>
</body>