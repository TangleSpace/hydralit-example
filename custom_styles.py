button_styles = """
.btn {
	 box-sizing: border-box;
	 appearance: none;
	 background-color: transparent;
	 border: 2px solid #e74c3c;
	 border-radius: 0.6em;
	 color: #e74c3c;
	 cursor: pointer;
	 display: flex;
	 align-self: center;
	 font-size: 1rem;
	 font-weight: 400;
	 line-height: 1;
	 margin: 20px;
	 padding: 1.2em 2.8em;
	 text-decoration: none;
	 text-align: center;
	 text-transform: uppercase;
	 font-family: 'Montserrat', sans-serif;
	 font-weight: 700;
}
 .btn:hover, .btn:focus {
	 color: #fff;
	 outline: 0;
}
 .first {
	 transition: box-shadow 300ms ease-in-out, color 300ms ease-in-out;
}
 .first:hover {
	 box-shadow: 0 0 40px 40px #e74c3c inset;
}
 .second {
	 border-radius: 3em;
	 border-color: #1abc9c;
	 color: #fff;
	 background-image: linear-gradient(to right, rgba(26, 188, 156, 0.6), rgba(26, 188, 156, 0.6) 5%, #1abc9c 5%, #1abc9c 10%, rgba(26, 188, 156, 0.6) 10%, rgba(26, 188, 156, 0.6) 15%, #1abc9c 15%, #1abc9c 20%, rgba(26, 188, 156, 0.6) 20%, rgba(26, 188, 156, 0.6) 25%, #1abc9c 25%, #1abc9c 30%, rgba(26, 188, 156, 0.6) 30%, rgba(26, 188, 156, 0.6) 35%, #1abc9c 35%, #1abc9c 40%, rgba(26, 188, 156, 0.6) 40%, rgba(26, 188, 156, 0.6) 45%, #1abc9c 45%, #1abc9c 50%, rgba(26, 188, 156, 0.6) 50%, rgba(26, 188, 156, 0.6) 55%, #1abc9c 55%, #1abc9c 60%, rgba(26, 188, 156, 0.6) 60%, rgba(26, 188, 156, 0.6) 65%, #1abc9c 65%, #1abc9c 70%, rgba(26, 188, 156, 0.6) 70%, rgba(26, 188, 156, 0.6) 75%, #1abc9c 75%, #1abc9c 80%, rgba(26, 188, 156, 0.6) 80%, rgba(26, 188, 156, 0.6) 85%, #1abc9c 85%, #1abc9c 90%, rgba(26, 188, 156, 0.6) 90%, rgba(26, 188, 156, 0.6) 95%, #1abc9c 95%, #1abc9c 100%);
	 background-position: 0 0;
	 background-size: 100%;
	 transition: background 300ms ease-in-out;
}
 .second:hover {
	 background-position: 100px;
}
 .third {
	 border-color: #3498db;
	 color: #fff;
	 box-shadow: 0 0 40px 40px #3498db inset, 0 0 0 0 #3498db;
	 transition: all 150ms ease-in-out;
}
 .third:hover {
	 box-shadow: 0 0 10px 0 #3498db inset, 0 0 10px 4px #3498db;
}
 .fourth {
	 border-color: #f1c40f;
	 color: #fff;
	 background-image: linear-gradient(45deg, #f1c40f 50%, transparent 50%);
	 background-position: 100%;
	 background-size: 400%;
	 transition: background 300ms ease-in-out;
}
 .fourth:hover {
	 background-position: 0;
}
 .fifth {
	 border-color: #8e44ad;
	 border-radius: 0;
	 color: #8e44ad;
	 position: relative;
	 overflow: hidden;
	 z-index: 1;
	 transition: color 150ms ease-in-out;
}
 .fifth:after {
	 content: '';
	 position: absolute;
	 display: block;
	 top: 0;
	 left: 50%;
	 transform: translateX(-50%);
	 width: 0;
	 height: 100%;
	 background: #8e44ad;
	 z-index: -1;
	 transition: width 150ms ease-in-out;
}
 .fifth:hover {
	 color: #fff;
}
 .fifth:hover:after {
	 width: 110%;
}
 .sixth {
	 border-radius: 3em;
	 border-color: #2ecc71;
	 color: #2ecc71;
	 background-image: linear-gradient(to bottom, transparent 50%, #2ecc71 50%);
	 background-position: 0% 0%;
	 background-size: 210%;
	 transition: background 150ms ease-in-out, color 150ms ease-in-out;
}
 .sixth:hover {
	 color: #fff;
	 background-position: 0 100%;
}
 
"""