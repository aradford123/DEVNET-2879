# coding: utf-8

# this line is required above as py2 interpets this as ascii otherwise and bails with a Non-ASCII character '\xc2' error
issue={
  "issueDetails" : {
    "issue" : [ {
      "issueId" : "AWPuxkGB_Vn43OLUwqjI",
      "issueSource" : "Cisco DNA",
      "issueCategory" : "Onboarding",
      "issueName" : "wireless_client_onboarding",
      "issueDescription" : "This client is taking longer than expected time to connect to 'sda' SSID due to excessive authentication time.<ul><li>Onboarding took 31.4 seconds seconds(expected time should be less than 10.0 seconds).</li><li>802.11 Association took less than a second (expected time should be less than 2.0 seconds).</li><li>Authentication and Key Exchange took less than a second (expected time should be less than 3.0 seconds)</li><li>IP Addressing took 0 seconds (expected time should be less than 5.0 seconds)</li><li>This client tried to onboard 1 times which took 31.1 seconds </li></ul><br>The authentication delay is because the client is slow to respond to authentication messages.The client was connecting to 'sda' SSID on 5.0 GHz radio on 'adam-sda-3802' AP  in 'Global/north sydney/level 22'. The AP was connected to '3504' WLC.",
      "issueEntity" : "Client",
      "issueEntityValue" : "00:26:08:E0:F4:97",
      "issueSeverity" : "HIGH",
      "issuePriority" : "",
      "issueSummary" : "Wireless client took a long time to connect (SSID: sda, AP: adam-sda-3802, Band: 5.0 GHz, Site: Global/north sydney/level 22) - Excessive time due to RF issues",
      "issueTimestamp" : 1528719213433,
      "suggestedActions" : [ {
        "message" : "Check whether the client moved during the authentication phase, since a moving client may cause packet losses and retries.",
        "steps" : [ ]
      }, {
        "message" : "Check for a recent OS update, since this may have been fixed in an update.",
        "steps" : [ ]
      }, {
        "message" : "Check the RF conditions at the client location. Since bad RF condition will leads to packet losses and higher retries.",
        "steps" : [ ]
      }, {
        "message" : "Check if fragmentation is occurring in the network, since this may lead to additional processing delays.",
        "steps" : [ ]
      }, {
        "message" : "Check WLC EAP Identity request timeout as the client may have not responded to this request in time.",
        "steps" : [ ]
      } ],
      "impactedHosts" : [ {
        "hostType" : "WIRELESS",
        "hostName" : "adams-MBP",
        "hostOs" : "Apple-Device",
        "ssid" : "sda",
        "connectedInterface" : "Unknown",
        "macAddress" : "00:26:08:E0:F4:97",
        "failedAttempts" : 1,
        "location" : {
          "siteId" : "305ed723-2e48-499b-a383-49103b15af54",
          "siteType" : "FLOOR",
          "area" : "Global",
          "building" : "north sydney",
          "floor" : "level 22",
          "apsImpacted" : [ "CC:16:7E:92:2B:40" ]
        },
        "timestamp" : 1528719213433
      } ]
    }, {
      "issueId" : "AWPuxGva_Vn43OLUwqjF",
      "issueSource" : "Cisco DNA",
      "issueCategory" : "Onboarding",
      "issueName" : "wireless_client_onboarding",
      "issueDescription" : None,
      "issueEntity" : "Client",
      "issueEntityValue" : "00:26:08:E0:F4:97",
      "issueSeverity" : "HIGH",
      "issuePriority" : "",
      "issueSummary" : "Wireless client failed to roam (SSID: sda, AP: adam-sda-3802, Band: 5.0 GHz, Site: Global/north sydney/level 22) - Failed to authenticate due to Client Timeout",
      "issueTimestamp" : 1528719093228,
      "suggestedActions" : [ {
        "message" : "Verify whether the client software has gone through a recent update since this may be a recent change of behavior.",
        "steps" : [ ]
      }, {
        "message" : "If the failed attempt is associated with a client that is located outdoors, consider introducing Low RSSI Threshold to the setup since this will force the client to join an AP with a stronger signal. Also check the AP location for RF Issues. Make sure the AP is in client's line of sight.",
        "steps" : [ ]
      } ],
      "impactedHosts" : [ {
        "hostType" : "WIRELESS",
        "hostName" : "adams-MBP",
        "hostOs" : "Apple-Device",
        "ssid" : "sda",
        "connectedInterface" : "Unknown",
        "macAddress" : "00:26:08:E0:F4:97",
        "failedAttempts" : 1,
        "location" : {
          "siteId" : "305ed723-2e48-499b-a383-49103b15af54",
          "siteType" : "FLOOR",
          "area" : "Global",
          "building" : "north sydney",
          "floor" : "level 22",
          "apsImpacted" : [ "CC:16:7E:92:2B:40" ]
        },
        "timestamp" : 1528719093228
      } ]
    }, {
      "issueId" : "AWPuwMML_Vn43OLUwqi9",
      "issueSource" : "Cisco DNA",
      "issueCategory" : "Onboarding",
      "issueName" : "wireless_client_onboarding",
      "issueDescription" : None,
      "issueEntity" : "Client",
      "issueEntityValue" : "00:26:08:E0:F4:97",
      "issueSeverity" : "HIGH",
      "issuePriority" : "",
      "issueSummary" : "Wireless client failed to roam (SSID: sda, AP: adam-sda-3802, Band: 5.0 GHz, Site: Unknown) - Failed to authenticate due to Client Timeout",
      "issueTimestamp" : 1528718854206,
      "suggestedActions" : [ {
        "message" : "Verify whether the client software has gone through a recent update since this may be a recent change of behavior.",
        "steps" : [ ]
      }, {
        "message" : "If the failed attempt is associated with a client that is located outdoors, consider introducing Low RSSI Threshold to the setup since this will force the client to join an AP with a stronger signal. Also check the AP location for RF Issues. Make sure the AP is in client's line of sight.",
        "steps" : [ ]
      } ],
      "impactedHosts" : [ {
        "hostType" : "WIRELESS",
        "hostName" : "adams-MBP",
        "hostOs" : "Apple-Device",
        "ssid" : "sda",
        "connectedInterface" : "Unknown",
        "macAddress" : "00:26:08:E0:F4:97",
        "failedAttempts" : 1,
        "location" : {
          "siteId" : "UNASSIGNED",
          "siteType" : "BUILDING",
          "area" : "Global",
          "building" : "UNASSIGNED",
          "floor" : None,
          "apsImpacted" : [ "CC:16:7E:92:2B:40" ]
        },
        "timestamp" : 1528718854206
      } ]
    }, {
      "issueId" : "AWPsCspD_Vn43OLUwqUd",
      "issueSource" : "Cisco DNA",
      "issueCategory" : "Onboarding",
      "issueName" : "wireless_client_onboarding",
      "issueDescription" : "This client is taking longer than expected time to connect to 'sda' SSID due to excessive authentication time.<ul><li>Onboarding took 29.8 seconds (expected time should be less than 10.0 seconds).</li><li>Association took less than a second (expected time should be less than 2.0 seconds)</li><li>Authentication and Key Exchange took 29.8 seconds (expected time should be less than 3.0 seconds)</li><li>IP Addressing took 0 seconds (expected time should be less than 5.0 seconds)</li></ul><br>The reason for the longer authentication time is delays from the AAA server or the network.The client itself is responding in time.The client was connecting to 'sda' SSID on 5.0 GHz radio on 'adam-sda-3802' AP in 'Global/north sydney/level 22'. The AP was connected to '3504' WLC.",
      "issueEntity" : "Client",
      "issueEntityValue" : "00:26:08:E0:F4:97",
      "issueSeverity" : "HIGH",
      "issuePriority" : "",
      "issueSummary" : "Wireless client took a long time to connect (SSID: sda, AP: adam-sda-3802, Band: 5.0 GHz) - Excessive time for Authentication due to AAA server or Network delays",
      "issueTimestamp" : 1528673434050,
      "suggestedActions" : [ {
        "message" : "Verify the network connectivity to the AAA server. Since there may be network glitch causing retries that leads to texcessive onboarding times.",
        "steps" : [ ]
      }, {
        "message" : "Verify whether the AAA server is responding to requests.",
        "steps" : [ ]
      }, {
        "message" : "Check the network load between the AP and the WLC, and between the WLC and the AAA server. Since excessive traffic can cause additional delays.",
        "steps" : [ ]
      } ],
      "impactedHosts" : [ {
        "hostType" : "WIRELESS",
        "hostName" : "adams-MBP",
        "hostOs" : "Apple-Device",
        "ssid" : "sda",
        "connectedInterface" : "Unknown",
        "macAddress" : "00:26:08:E0:F4:97",
        "failedAttempts" : 1,
        "location" : {
          "siteId" : "305ed723-2e48-499b-a383-49103b15af54",
          "siteType" : "FLOOR",
          "area" : "Global",
          "building" : "north sydney",
          "floor" : "level 22",
          "apsImpacted" : [ "CC:16:7E:92:2B:40" ]
        },
        "timestamp" : 1528673434050
      } ]
    } ]
  }
}