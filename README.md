# [WIP] Versio Domain Checker

If you need a Versio account and want to support me, please use this referral link: [https://www.versio.nl/?pa=104758hfsce](https://www.versio.nl/?pa=104758hfsce)

## About
Versio Domain Checker is a simple script that checks if a domain is available on versio.nl.
If the domain is available the domain will be registered and a notification will be sent.

## Configuration
Use the config.yaml.example to create your own configuration.  
Use the .env.example file to create your own .env and enter your keys or use environment variables.

## Steps in script
1. Read yaml file
2. Get a list of already registered domain names
3. Get the status for all domains in the yaml that aren't already registered by the user.
4. Register all domain names that are available
5. Send a notification containing all registered domains

