[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0c2ec4f5e9ad4a96bca8033b5c54e66a)](https://www.codacy.com/app/ONS-Digital/business-index-ui?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ONSdigital/splunk-api&amp;utm_campaign=Badge_Grade) [![Bitbucket issues](https://img.shields.io/bitbucket/issues/ONSdigital/splunk-api.svg)]() [![license](https://img.shields.io/github/license/ONSdigital/splunk-api.svg)]() 

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
- 'JavaScript actions' - Some actions may not be operational and thus require JavaScript files to be properly uploaded and modified if needed, please see Splunk documentation for more information.
- 'indexes' - The project uses a mixture of both index and sourcetype as identifiers to eliminate overhead.
- 'rest data input' - health check, collector???
