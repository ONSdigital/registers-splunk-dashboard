# Splunk Performance Dashboard


### Description
A series of XML scripted files to generate dashboards for the Business Index project.


### Prerequisites
* Splunk Enterprise account or a local instance of Splunk ([Download](https://www.splunk.com/en_us/download/splunk-enterprise.html))


### Development Setup (MacOS)
Copy the views files under the local or enterprise directory;
```shell
sudo cp [file location] [app]/local/data/ui/views
```
Similarly copy the assets and static files to the following location;
```shell
sudo cp [file location] [app]/appserver/static
```

Note: You may not require sudo privileges for such trivial tasks.


### Notes:
- 'JavaScript actions' - Some action may not be operational and thus require JavaScript files to be properly uploaded and modified if needed, please see Splunk documentation for more information.
- 'indexes' - The project uses a mixture of both index and sourcetype as identifiers to eliminate overhead.
- 'rest data input' -
