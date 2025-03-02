LOCATION_URL="https://api.tequila.kiwi.com/locations/query"
SEARCH_URL="https://api.tequila.kiwi.com/v2/search?"
BASE_AIRPORT="WAW"
CURRENCY="PLN"
AIRPORT_CODES=[
    'ANR', 'BRU', 'CRL', 'LGG', 'OST', 'AJA', 'BIA', 'BVA', 'EGC', 'BZR', 'BIQ', 'BOD',
    'BES', 'CCF', 'XCR', 'CMF', 'DNR', 'FSC', 'GNB', 'LRH', 'LIL', 'LIG', 'LYS', 'MRS',
    'BSL', 'NTE', 'NCE', 'FNI', 'CDG', 'ORY', 'PUF', 'PGF', 'PIS', 'RDZ', 'EBU', 'SXB',
    'TLN', 'TLS', 'TUF', 'GIB', 'GCI', 'JER', 'ORK', 'DUB', 'KIR', 'NOC', 'SNN', 'IOM',
    'LUX', 'AMS', 'EIN', 'GRQ', 'MST', 'RTM', 'BYJ', 'FAO', 'FNC', 'PXO', 'LIS', 'OPO',
    'PDL', 'TER', 'LCG', 'ALC', 'LEI', 'OVD', 'BCN', 'FUE', 'GRO', 'LPA', 'GRX', 'HSK',
    'IBZ', 'XRY', 'SPC', 'ACE', 'ILD', 'MAD', 'AGP', 'MAH', 'MJV', 'PMI', 'REU', 'SDR',
    'SCQ', 'SVQ', 'TFN', 'TFS', 'VLC', 'VLL', 'ZAZ', 'GRZ', 'KLU', 'INN', 'LNZ', 'SZG',
    'VIE', 'FKB', 'TXL', 'SXF', 'BER', 'BRE', 'CGN', 'DTM', 'DUS', 'FRA', 'HHN', 'MLH',
    'BSL', 'EAP', 'FDH', 'HAM', 'HAJ', 'LEJ', 'LBC', 'FMM', 'MUC', 'NUE', 'STR', 'NRN',
    'ATH', 'CHQ', 'JKH', 'CFU', 'HER', 'KLX', 'AOK', 'KVA', 'EFL', 'KGS', 'JMK', 'MJT',
    'PVK', 'RHO', 'SMI', 'JTR', 'JSI', 'SKU', 'SKG', 'VOL', 'ZTH', 'AHO', 'AOI', 'BRI',
    'BGY', 'BLQ', 'VBS', 'BDS', 'CAG', 'CTA', 'CUF', 'FLR', 'GOA', 'SUF', 'LIN', 'MXP',
    'NAP', 'OLB', 'PMO', 'PEG', 'PSR', 'PSA', 'RMI', 'FCO', 'CIA', 'TPS', 'TRS', 'TRN',
    'VCE', 'VRN', 'BSL', 'BRN', 'GVA', 'ACH', 'ZRH', 'BZG', 'GDN', 'KTW', 'KRK', 'LUZ',
    'LCJ', 'POZ', 'RZE', 'SZZ', 'WAW', 'WMI', 'WRO', 'OTP', 'CLJ', 'CND', 'IAS', 'OMR',
    'SBZ', 'TSR', 'TIA', 'EVN', 'LWN', 'GYD', 'KVD', 'NAJ', 'GBB', 'LLK', 'GNA', 'GME',
    'MSQ', 'BNX', 'SJJ', 'TZL', 'OMO', 'BOJ', 'PDV', 'SOF', 'VAR', 'DBV', 'ZAG', 'OSI',
    'PUY', 'RJK', 'SPU', 'ZAD', 'LCA', 'PFO', 'ECN', 'BRQ', 'KLV', 'OSR', 'PRG', 'PED',
    'TLL', 'TAY', 'UGA', 'BUS', 'KUT', 'UGM', 'UGS', 'SUI', 'TBS', 'BUD', 'DEB', 'SOB',
    'QGY', 'QPJ', 'PRN', 'RIX', 'VNT', 'KUN', 'PLQ', 'SQQ', 'VNO', 'OHD', 'SKP', 'MLA',
    'KIV', 'TGD', 'TIV', 'ABA', 'DYR', 'AAQ', 'ARH', 'ASF', 'BAX', 'EGO', 'BQS', 'BTK',
    'BZK', 'CSY', 'CEK', 'CEE', 'HTA', 'ESL', 'IKT', 'GRV', 'KGD', 'KZN', 'KHV', 'KXK',
    'KRR', 'KJA', 'URS', 'GDX', 'MQF', 'MCX', 'MRV', 'DME', 'SVO', 'VKO', 'MMK', 'NAL',
    'NJC', 'NBC', 'GOJ', 'NOZ', 'OVB', 'OMS', 'REN', 'OSW', 'PEE', 'PES', 'PVS', 'PKC',
    'PKV', 'ROV', 'LED', 'KUF', 'RTW', 'AER', 'STW', 'SGC', 'SCW', 'TOF', 'TJM', 'UUD',
    'ULY', 'UFA', 'VVO', 'OGZ', 'VOG', 'VOZ', 'YKS', 'IAR', 'SVX', 'UUS', 'BEG', 'INI',
    'BTS', 'KSC', 'PZY', 'TAT', 'SLD', 'ILZ', 'LJU', 'MBX', 'POW', 'ADA', 'ESB', 'AYT',
    'BJV', 'YEI', 'DLM', 'GZT', 'IST', 'SAW', 'ADB', 'ASR', 'KYA', 'KZR', 'MLX', 'NAV',
    'SZF', 'TZX', 'ONQ', 'KBP', 'CWC', 'DOK', 'DNK', 'GML', 'IFO', 'HRK', 'KWG', 'IEV',
    'VSG', 'LWO', 'NLV', 'ODS', 'SIP', 'OZH', 'AAL', 'AAR', 'BLL', 'CPH', 'FAE', 'MHQ',
    'HEL', 'KTT', 'KUO', 'KAO', 'LPP', 'OUL', 'RVN', 'TMP', 'TKU', 'VAA', 'AEY', 'KEF',
    'RKV', 'AES', 'BGO', 'BOO', 'HAU', 'KRS', 'KSU', 'OSL', 'RYG', 'TRF', 'SVG', 'TOS',
    'TRD', 'GSE', 'GOT', 'LLA', 'MMX', 'NRK', 'OSD', 'ARN', 'BMA', 'NYO', 'VST', 'UME',
    'VXO', 'VBY', 'BHX', 'BOH', 'BRS', 'CWL', 'DSA', 'MME', 'EMA', 'EXT', 'LBA', 'LPL',
    'LCY', 'LGW', 'LHR', 'LTN', 'SEN', 'STN', 'MAN', 'NCL', 'NQY', 'NWI', 'SOU', 'ABZ',
    'EDI', 'GLA', 'PIK', 'INV', 'BFS', 'BHD', 'LDY',
]
