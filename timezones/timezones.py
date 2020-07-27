from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

timezones = [
               {
                 "id": 1,
                 "timezone": "ACDT",
                 "name": "Australian Central Daylight Savings Time",
                 "UTCOffset": "+10:30"
               },
               {
                 "id": 2,
                 "timezone": "ACST",
                 "name": "Australian Central Standard Time",
                 "UTCOffset": "+9:30"
               },
               {
                 "id": 3,
                 "timezone": "ACT",
                 "name": "Acre Time",
                 "UTCOffset": -5
               },
               {
                 "id": 4,
                 "timezone": "ACWST",
                 "name": "Australian Central Western Standard Time",
                 "UTCOffset": "+8:45"
               },
               {
                 "id": 5,
                 "timezone": "ADT",
                 "name": "Atlantic Daylight Time",
                 "UTCOffset": -3
               },
               {
                 "id": 6,
                 "timezone": "AEDT",
                 "name": "Australian Eastern Daylight Savings Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 7,
                 "timezone": "AEST",
                 "name": "Australian Eastern Standard Time",
                 "UTCOffset": "+10"
               },
               {
                 "id": 8,
                 "timezone": "AFT",
                 "name": "Afghanistan Time",
                 "UTCOffset": "+4:30"
               },
               {
                 "id": 9,
                 "timezone": "AKDT",
                 "name": "Alaska Daylight Time",
                 "UTCOffset": "-8"
               },
               {
                 "id": 10,
                 "timezone": "AKST",
                 "name": "Alaska Standard Time",
                 "UTCOffset": "-9"
               },
               {
                 "id": 11,
                 "timezone": "AMST",
                 "name": "Amazon Summer Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 12,
                 "timezone": "AMT",
                 "name": "Amazon Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 13,
                 "timezone": "AMT",
                 "name": "Armenia Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 14,
                 "timezone": "ART",
                 "name": "Argentina Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 15,
                 "timezone": "AST",
                 "name": "Atlantic Standard Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 16,
                 "timezone": "AST",
                 "name": "Arabia Standard Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 18,
                 "timezone": "AWST",
                 "name": "Australian Western Standard Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 19,
                 "timezone": "AZOST",
                 "name": "Azores Summer Time",
                 "UTCOffset": "+0"
               },
               {
                 "id": 20,
                 "timezone": "AZOT",
                 "name": "Azores Standard Time",
                 "UTCOffset": "-1"
               },
               {
                 "id": 21,
                 "timezone": "AZT",
                 "name": "Azerbaijan Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 22,
                 "timezone": "BDT",
                 "name": "Brunei Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 23,
                 "timezone": "BIT",
                 "name": "Baker Island Time",
                 "UTCOffset": "-12"
               },
               {
                 "id": 24,
                 "timezone": "BNT",
                 "name": "Brunei Darussalam Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 25,
                 "timezone": "BOT",
                 "name": "Bolivia Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 26,
                 "timezone": "BRST",
                 "name": "Brasilia Summer Time",
                 "UTCOffset": "-2"
               },
               {
                 "id": 27,
                 "timezone": "BRT",
                 "name": "Brasilia Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 28,
                 "timezone": "BST",
                 "name": "British Summer Time",
                 "UTCOffset": "+1"
               },
               {
                 "id": 29,
                 "timezone": "BST",
                 "name": "Bangladesh Standard Time",
                 "UTCOffset": "+6"
               },
               {
                 "id": 30,
                 "timezone": "BST",
                 "name": "Bougainville Standard Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 31,
                 "timezone": "BTT",
                 "name": "Bhutan Time",
                 "UTCOffset": "+6"
               },
               {
                 "id": 32,
                 "timezone": "CAT",
                 "name": "Central Africa Time",
                 "UTCOffset": "+2"
               },
               {
                 "id": 33,
                 "timezone": "CCT",
                 "name": "Cocos Islands Time",
                 "UTCOffset": "+6:30"
               },
               {
                 "id": 34,
                 "timezone": "CDT",
                 "name": "Central Daylight Time",
                 "UTCOffset": "-5"
               },
               {
                 "id": 35,
                 "timezone": "CDT",
                 "name": "Cuba Daylight Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 36,
                 "timezone": "CEST",
                 "name": "Central European Summer Time",
                 "UTCOffset": "+2"
               },
               {
                 "id": 37,
                 "timezone": "CET",
                 "name": "Central European Time",
                 "UTCOffset": "+1"
               },
               {
                 "id": 38,
                 "timezone": "CHADT",
                 "name": "Chatham Daylight Time",
                 "UTCOffset": "+13:45"
               },
               {
                 "id": 39,
                 "timezone": "CHAST",
                 "name": "Chatham Standard Time",
                 "UTCOffset": "+12:45"
               },
               {
                 "id": 40,
                 "timezone": "CHOST",
                 "name": "Choibalsan Summer Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 41,
                 "timezone": "CHOT",
                 "name": "Choibalsan Standard Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 42,
                 "timezone": "CHST",
                 "name": "Chamorro Standard Time",
                 "UTCOffset": "+10"
               },
               {
                 "id": 43,
                 "timezone": "CHUT",
                 "name": "Chuuk Time",
                 "UTCOffset": "+10"
               },
               {
                 "id": 44,
                 "timezone": "CIST",
                 "name": "Clipperton Island Standard Time",
                 "UTCOffset": "-8"
               },
               {
                 "id": 45,
                 "timezone": "CIT",
                 "name": "Central Indonesia Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 46,
                 "timezone": "CKT",
                 "name": "Cook Island Time",
                 "UTCOffset": "-10"
               },
               {
                 "id": 47,
                 "timezone": "CLST",
                 "name": "Chile Summer Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 48,
                 "timezone": "CLT",
                 "name": "Chile Standard Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 49,
                 "timezone": "COST",
                 "name": "Colombia Summer Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 50,
                 "timezone": "COT",
                 "name": "Colombia Time",
                 "UTCOffset": "-5"
               },
               {
                 "id": 51,
                 "timezone": "CST",
                 "name": "Central Standard Time",
                 "UTCOffset": "-6"
               },
               {
                 "id": 52,
                 "timezone": "CST",
                 "name": "Cuba Standard Time",
                 "UTCOffset": "-5"
               },
               {
                 "id": 53,
                 "timezone": "CST",
                 "name": "China Standard Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 55,
                 "timezone": "CVT",
                 "name": "Cape Verde Time",
                 "UTCOffset": "-1"
               },
               {
                 "id": 56,
                 "timezone": "CWST",
                 "name": "Central Western Standard Time",
                 "UTCOffset": "+8:45"
               },
               {
                 "id": 57,
                 "timezone": "CXT",
                 "name": "Christmas Island Time",
                 "UTCOffset": "+7"
               },
               {
                 "id": 58,
                 "timezone": "DAVT",
                 "name": "Davis Time",
                 "UTCOffset": "+7"
               },
               {
                 "id": 59,
                 "timezone": "DDUT",
                 "name": "Dumont d'Urville Time",
                 "UTCOffset": "+10"
               },
               {
                 "id": 60,
                 "timezone": "EASST",
                 "name": "Easter Island Summer Time",
                 "UTCOffset": "-5"
               },
               {
                 "id": 61,
                 "timezone": "EAST",
                 "name": "Easter Island Standard Time",
                 "UTCOffset": "-6"
               },
               {
                 "id": 62,
                 "timezone": "EAT",
                 "name": "East Africa Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 63,
                 "timezone": "ECT",
                 "name": "Ecuador Time",
                 "UTCOffset": "-5"
               },
               {
                 "id": 64,
                 "timezone": "EDT",
                 "name": "Eastern Daylight Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 65,
                 "timezone": "EEST",
                 "name": "Eastern European Summer Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 66,
                 "timezone": "EET",
                 "name": "Eastern European Time",
                 "UTCOffset": "+2"
               },
               {
                 "id": 67,
                 "timezone": "EGST",
                 "name": "Eastern Greenland Summer Time",
                 "UTCOffset": "+0"
               },
               {
                 "id": 68,
                 "timezone": "EGT",
                 "name": "Eastern Greenland Time",
                 "UTCOffset": "-1"
               },
               {
                 "id": 69,
                 "timezone": "EIT",
                 "name": "Eastern Indonesian Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 70,
                 "timezone": "EST",
                 "name": "Eastern Standard Time",
                 "UTCOffset": "-5"
               },
               {
                 "id": 72,
                 "timezone": "FET",
                 "name": "Further-eastern European Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 73,
                 "timezone": "FJT",
                 "name": "Fiji Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 74,
                 "timezone": "FKST",
                 "name": "Falkland Islands Summer Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 75,
                 "timezone": "FKT",
                 "name": "Falkland Islands Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 76,
                 "timezone": "FNT",
                 "name": "Fernando de Noronha Time",
                 "UTCOffset": "-2"
               },
               {
                 "id": 77,
                 "timezone": "GALT",
                 "name": "Galapagos Time",
                 "UTCOffset": "-6"
               },
               {
                 "id": 78,
                 "timezone": "GAMT",
                 "name": "Gambier Islands",
                 "UTCOffset": "-9"
               },
               {
                 "id": 79,
                 "timezone": "GET",
                 "name": "Georgia Standard Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 80,
                 "timezone": "GFT",
                 "name": "French Guiana Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 81,
                 "timezone": "GILT",
                 "name": "Gilbert Island Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 82,
                 "timezone": "GIT",
                 "name": "Gambier Island Time",
                 "UTCOffset": "-9"
               },
               {
                 "id": 83,
                 "timezone": "GMT",
                 "name": "Greenwich Mean Time",
                 "UTCOffset": "+0"
               },
               {
                 "id": 84,
                 "timezone": "GST",
                 "name": "Gulf Standard Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 85,
                 "timezone": "GST",
                 "name": "South Georgia Time",
                 "UTCOffset": "-2"
               },
               {
                 "id": 86,
                 "timezone": "GYT",
                 "name": "Guyana Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 87,
                 "timezone": "HADT",
                 "name": "Hawaii-Aleutian Daylight Time",
                 "UTCOffset": "-9"
               },
               {
                 "id": 88,
                 "timezone": "HAST",
                 "name": "Hawaii-Aleutian Standard Time",
                 "UTCOffset": "-10"
               },
               {
                 "id": 89,
                 "timezone": "HKT",
                 "name": "Hong Kong Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 90,
                 "timezone": "HMT",
                 "name": "Heard and McDonald Islands Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 91,
                 "timezone": "HOVST",
                 "name": "Khovd Summer Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 92,
                 "timezone": "HOVT",
                 "name": "Khovd Standard Time",
                 "UTCOffset": "+7"
               },
               {
                 "id": 93,
                 "timezone": "ICT",
                 "name": "Indochina Time",
                 "UTCOffset": "+7"
               },
               {
                 "id": 94,
                 "timezone": "IDT",
                 "name": "Israel Daylight Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 95,
                 "timezone": "IOT",
                 "name": "Indian Chagos Time",
                 "UTCOffset": "+6"
               },
               {
                 "id": 96,
                 "timezone": "IRDT",
                 "name": "Iran Daylight Time",
                 "UTCOffset": "+4:30"
               },
               {
                 "id": 97,
                 "timezone": "IRKT",
                 "name": "Irkutsk Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 98,
                 "timezone": "IRST",
                 "name": "Iran Standard Time",
                 "UTCOffset": "+3:30"
               },
               {
                 "id": 99,
                 "timezone": "IST",
                 "name": "Indian Standard Time",
                 "UTCOffset": "+5:30"
               },
               {
                 "id": 100,
                 "timezone": "IST",
                 "name": "Irish Standard Time",
                 "UTCOffset": "+1"
               },
               {
                 "id": 101,
                 "timezone": "IST",
                 "name": "Israel Standard Time",
                 "UTCOffset": "+2"
               },
               {
                 "id": 102,
                 "timezone": "JST",
                 "name": "Japan Standard Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 103,
                 "timezone": "KGT",
                 "name": "Kyrgyzstan time",
                 "UTCOffset": "+6"
               },
               {
                 "id": 104,
                 "timezone": "KOST",
                 "name": "Kosrae Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 105,
                 "timezone": "KRAT",
                 "name": "Krasnoyarsk Time",
                 "UTCOffset": "+7"
               },
               {
                 "id": 106,
                 "timezone": "KST",
                 "name": "Korea Standard Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 107,
                 "timezone": "LHDT",
                 "name": "Lord Howe Daylight Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 108,
                 "timezone": "LHST",
                 "name": "Lord Howe Standard Time",
                 "UTCOffset": "+10:30"
               },
               {
                 "id": 109,
                 "timezone": "LINT",
                 "name": "Line Islands Time",
                 "UTCOffset": "+14"
               },
               {
                 "id": 110,
                 "timezone": "MAGT",
                 "name": "Magadan Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 111,
                 "timezone": "MART",
                 "name": "Marquesas Islands Time",
                 "UTCOffset": "-9:30"
               },
               {
                 "id": 112,
                 "timezone": "MAWT",
                 "name": "Mawson Station Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 113,
                 "timezone": "MDT",
                 "name": "Mountain Daylight Time",
                 "UTCOffset": "-6"
               },
               {
                 "id": 114,
                 "timezone": "MHT",
                 "name": "Marshall Islands",
                 "UTCOffset": "+12"
               },
               {
                 "id": 115,
                 "timezone": "MIST",
                 "name": "Macquarie Island Station Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 116,
                 "timezone": "MIT",
                 "name": "Marquesas Islands Time",
                 "UTCOffset": "-9:30"
               },
               {
                 "id": 117,
                 "timezone": "MMT",
                 "name": "Myanmar Standard Time",
                 "UTCOffset": "+6:30"
               },
               {
                 "id": 118,
                 "timezone": "MSK",
                 "name": "Moscow Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 119,
                 "timezone": "MST",
                 "name": "Mountain Standard Time",
                 "UTCOffset": "-7"
               },
               {
                 "id": 120,
                 "timezone": "MST",
                 "name": "Malaysia Standard Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 122,
                 "timezone": "MUT",
                 "name": "Mauritius Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 123,
                 "timezone": "MVT",
                 "name": "Maldives Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 124,
                 "timezone": "MYT",
                 "name": "Malaysia Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 125,
                 "timezone": "NCT",
                 "name": "New Caledonia Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 126,
                 "timezone": "NDT",
                 "name": "Newfoundland Daylight Time",
                 "UTCOffset": "-2:30"
               },
               {
                 "id": 127,
                 "timezone": "NFT",
                 "name": "Norfolk Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 128,
                 "timezone": "NPT",
                 "name": "Nepal Time",
                 "UTCOffset": "+5:45"
               },
               {
                 "id": 129,
                 "timezone": "NRT",
                 "name": "Nauru Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 130,
                 "timezone": "NST",
                 "name": "Newfoundland Standard Time",
                 "UTCOffset": "-3:30"
               },
               {
                 "id": 131,
                 "timezone": "NT",
                 "name": "Newfoundland Time",
                 "UTCOffset": "-3:30"
               },
               {
                 "id": 132,
                 "timezone": "NUT",
                 "name": "Niue Time",
                 "UTCOffset": "-11"
               },
               {
                 "id": 133,
                 "timezone": "NZDT",
                 "name": "New Zealand Daylight Time",
                 "UTCOffset": "+13"
               },
               {
                 "id": 134,
                 "timezone": "NZST",
                 "name": "New Zealand Standard Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 135,
                 "timezone": "OMST",
                 "name": "Omsk Time",
                 "UTCOffset": "+6"
               },
               {
                 "id": 136,
                 "timezone": "ORAT",
                 "name": "Oral Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 137,
                 "timezone": "PDT",
                 "name": "Pacific Daylight Time",
                 "UTCOffset": "-7"
               },
               {
                 "id": 138,
                 "timezone": "PET",
                 "name": "Peru Time",
                 "UTCOffset": "-5"
               },
               {
                 "id": 139,
                 "timezone": "PETT",
                 "name": "Kamchatka Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 140,
                 "timezone": "PGT",
                 "name": "Papua New Guinea Time",
                 "UTCOffset": "+10"
               },
               {
                 "id": 141,
                 "timezone": "PHOT",
                 "name": "Phoenix Island Time",
                 "UTCOffset": "+13"
               },
               {
                 "id": 142,
                 "timezone": "PHT",
                 "name": "Philippine Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 143,
                 "timezone": "PKT",
                 "name": "Pakistan Standard Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 144,
                 "timezone": "PMDT",
                 "name": "Saint Pierre and Miquelon Daylight time",
                 "UTCOffset": "-2"
               },
               {
                 "id": 145,
                 "timezone": "PMST",
                 "name": "Saint Pierre and Miquelon Standard Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 146,
                 "timezone": "PONT",
                 "name": "Pohnpei Standard Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 147,
                 "timezone": "PST",
                 "name": "Pacific Standard Time",
                 "UTCOffset": "-8"
               },
               {
                 "id": 148,
                 "timezone": "PST",
                 "name": "Philippine Standard Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 150,
                 "timezone": "PWT",
                 "name": "Palau Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 151,
                 "timezone": "PYST",
                 "name": "Paraguay Summer Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 152,
                 "timezone": "PYT",
                 "name": "Paraguay Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 153,
                 "timezone": "RET",
                 "name": "Réunion Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 154,
                 "timezone": "ROTT",
                 "name": "Rothera Research Station Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 155,
                 "timezone": "SAKT",
                 "name": "Sakhalin Island time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 156,
                 "timezone": "SAMT",
                 "name": "Samara Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 157,
                 "timezone": "SAST",
                 "name": "South African Standard Time",
                 "UTCOffset": "+2"
               },
               {
                 "id": 158,
                 "timezone": "SBT",
                 "name": "Solomon Islands Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 159,
                 "timezone": "SCT",
                 "name": "Seychelles Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 160,
                 "timezone": "SGT",
                 "name": "Singapore Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 161,
                 "timezone": "SLST",
                 "name": "Sri Lanka Standard Time",
                 "UTCOffset": "+5:30"
               },
               {
                 "id": 162,
                 "timezone": "SRET",
                 "name": "Srednekolymsk Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 163,
                 "timezone": "SRT",
                 "name": "Suriname Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 164,
                 "timezone": "SST",
                 "name": "Samoa Standard Time",
                 "UTCOffset": "-11"
               },
               {
                 "id": 165,
                 "timezone": "SYOT",
                 "name": "Showa Station Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 166,
                 "timezone": "TAHT",
                 "name": "Tahiti Time",
                 "UTCOffset": "-10"
               },
               {
                 "id": 167,
                 "timezone": "TFT",
                 "name": "French Southern and Antarctic Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 168,
                 "timezone": "THA",
                 "name": "Thailand Standard Time",
                 "UTCOffset": "+7"
               },
               {
                 "id": 169,
                 "timezone": "TJT",
                 "name": "Tajikistan Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 170,
                 "timezone": "TKT",
                 "name": "Tokelau Time",
                 "UTCOffset": "+13"
               },
               {
                 "id": 171,
                 "timezone": "TLT",
                 "name": "Timor Leste Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 172,
                 "timezone": "TMT",
                 "name": "Turkmenistan Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 173,
                 "timezone": "TOT",
                 "name": "Tonga Time",
                 "UTCOffset": "+13"
               },
               {
                 "id": 174,
                 "timezone": "TRT",
                 "name": "Turkey Time",
                 "UTCOffset": "+3"
               },
               {
                 "id": 175,
                 "timezone": "TVT",
                 "name": "Tuvalu Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 176,
                 "timezone": "ULAST",
                 "name": "Ulaanbaatar Summer Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 177,
                 "timezone": "ULAT",
                 "name": "Ulaanbaatar Standard Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 178,
                 "timezone": "USZ1",
                 "name": "Kaliningrad Time",
                 "UTCOffset": "+2"
               },
               {
                 "id": 179,
                 "timezone": "UTC",
                 "name": "Coordinated Universal Time",
                 "UTCOffset": "+0"
               },
               {
                 "id": 180,
                 "timezone": "UYST",
                 "name": "Uruguay Summer Time",
                 "UTCOffset": "-2"
               },
               {
                 "id": 181,
                 "timezone": "UYT",
                 "name": "Uruguay Standard Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 182,
                 "timezone": "UZT",
                 "name": "Uzbekistan Time",
                 "UTCOffset": "+5"
               },
               {
                 "id": 183,
                 "timezone": "VET",
                 "name": "Venezuelan Standard Time",
                 "UTCOffset": "-4"
               },
               {
                 "id": 184,
                 "timezone": "VLAT",
                 "name": "Vladivostok Time",
                 "UTCOffset": "+10"
               },
               {
                 "id": 185,
                 "timezone": "VOLT",
                 "name": "Volgograd Time",
                 "UTCOffset": "+4"
               },
               {
                 "id": 186,
                 "timezone": "VOST",
                 "name": "Vostok Station Time",
                 "UTCOffset": "+6"
               },
               {
                 "id": 187,
                 "timezone": "VUT",
                 "name": "Vanuatu Time",
                 "UTCOffset": "+11"
               },
               {
                 "id": 188,
                 "timezone": "WAKT",
                 "name": "Wake Island Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 189,
                 "timezone": "WAST",
                 "name": "West Africa Summer Time",
                 "UTCOffset": "+2"
               },
               {
                 "id": 190,
                 "timezone": "WAT",
                 "name": "West Africa Time",
                 "UTCOffset": "+1"
               },
               {
                 "id": 191,
                 "timezone": "WEST",
                 "name": "Western European Summer Time",
                 "UTCOffset": "+1"
               },
               {
                 "id": 192,
                 "timezone": "WET",
                 "name": "Western European Time",
                 "UTCOffset": "+0"
               },
               {
                 "id": 193,
                 "timezone": "WFT",
                 "name": "Wallis and Futuna Time",
                 "UTCOffset": "+12"
               },
               {
                 "id": 194,
                 "timezone": "WGST",
                 "name": "West Greenland Time",
                 "UTCOffset": "-3"
               },
               {
                 "id": 195,
                 "timezone": "WGST",
                 "name": "West Greenland Summer Time",
                 "UTCOffset": "-2"
               },
               {
                 "id": 196,
                 "timezone": "WIB",
                 "name": "Western Indonesia Time",
                 "UTCOffset": "+7"
               },
               {
                 "id": 197,
                 "timezone": "WIT",
                 "name": "Eastern Indonesia Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 198,
                 "timezone": "WST",
                 "name": "Western Standard Time",
                 "UTCOffset": "+8"
               },
               {
                 "id": 199,
                 "timezone": "YAKT",
                 "name": "Yakutsk Time",
                 "UTCOffset": "+9"
               },
               {
                 "id": 200,
                 "timezone": "YEKT",
                 "name": "Yekaterinburg Time",
                 "UTCOffset": "+5"
               }
             ]

@app.route('/')
def home():
    return 'Welcome to Timezones API'
app.run(host='0.0.0.0', debug=True)