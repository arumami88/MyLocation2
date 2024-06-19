/* Config Sample
 *
 * For more information on how you can configure this file
 * see https://docs.magicmirror.builders/configuration/introduction.html
 * and https://docs.magicmirror.builders/modules/configuration.html
 *
 * You can use environment variables using a `config.js.template` file instead of `config.js`
 * which will be converted to `config.js` while starting. For more information
 * see https://docs.magicmirror.builders/configuration/introduction.html#enviromnent-variables
 */
let config = {
	address: "localhost",	// Address to listen on, can be:
							// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
							// - another specific IPv4/6 to listen on a specific interface
							// - "0.0.0.0", "::" to listen on any interface
							// Default, when address config is left out or empty, is "localhost"
	port: 8080,
	basePath: "/",	// The URL path where MagicMirror² is hosted. If you are using a Reverse proxy
									// you must set the sub path here. basePath must end with a /
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"],	// Set [] to allow all IP addresses
									// or add a specific IPv4 of 192.168.1.5 :
									// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
									// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
									// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false,			// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "",	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "",	// HTTPS Certificate path, only require when useHttps is true

	language: "ja",
	locale: "ja-JP.UTF-8",
	logLevel: [], // Add "DEBUG" for even more logging
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar_monthly",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "Holidays",
			position: "top_left",
			config: {
				calendars: [
					{
						fetchInterval: 7 * 24 * 60 * 60 * 1000,
						symbol: "calendar-check",
						url: "https://www.google.com/calendar/ical/ja.japanese%23holiday%40group.v.calendar.google.com/public/basic.ics",
						maximumEntries: 3,
					}
				],
				fade: false,
			}
		},
		{
			module: "compliments",
			disabled: true,
			position: "lower_third"
		},
		{
			module: "MMM-SimpleText",
			position: "top_center",
			config: {
				text: {
					"value": "　　WHEREABOUTS"
					},
			},
		},
		{
			module: "MMM-SmartWebDisplay",
			position: "middle_center",
			config: {
				url: ["http://192.168.254.1/"],
				height: "500px",
				width: "500px",
				updateInterval: 0.5,
				displayLastUpdate: false,
				scrolling: "no",
			},
		},
		{
			module: "weather",
			position: "top_right",
			config: {
				weatherProvider: "openweathermap",
				type: "current",
				location: "Kanazawa",
				locationID: "1860243",
				apiKey: "XXXXXX"
			}
		},
		{
			module: "weather",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				weatherProvider: "openweathermap",
				type: "forecast",
				location: "Kanazawa",
				locationID: "1860243",
				apiKey: "XXXXXX",
				fade: false,
			}
		},
		{
			module: "MMM-MoonPhase",
			position: "top_right",
			config: {
				updateInterval: 432000000,
				hemisphere: "N",
				resolution: "detailed",
				basicColor: "white",
				title: "true",
				phase: "true",
				size: 100,
				moonAlign: "center",
				textAlign: "center",
				alpha: 0.7,
				riseAndSet: {
					display: false,
					lon: -80.0,
					lat: 40.0,
					gmtOffset: -3.0
				}
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "NHK News",
						url: "https://www.nhk.or.jp/rss/news/cat0.xml"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		},
	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") { module.exports = config; }
