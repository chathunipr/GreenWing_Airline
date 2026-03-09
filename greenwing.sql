
CREATE DATABASE greenwing;

USE greenwing;

CREATE TABLE users (
    userid INT AUTO_INCREMENT PRIMARY KEY,          -- unique ID for each user
    name VARCHAR(100) NOT NULL,                     -- user's name
    home_airport VARCHAR(100),                      -- user's home airport
    current_budget DECIMAL(12,2) DEFAULT 500000.00, -- starting budget
    total_profit DECIMAL(12,2) DEFAULT 0.00,       -- total profit earned
    total_co2 DECIMAL(12,2) DEFAULT 0.00,         -- total CO2 produced
    reputation INT DEFAULT 75                       -- user's reputation score
);


CREATE TABLE routes (
    routeid CHAR(4) PRIMARY KEY,                  -- unique ID for each route
    name VARCHAR(150),                            -- name of the route
    latitude_deg DECIMAL(10,6),                   -- latitude of the airport
    longitude_deg DECIMAL(10,6),                  -- longitude of the airport
    location VARCHAR(100),                        -- airport location
    airport_fee FLOAT DEFAULT 0,                  -- fee at the airport
    fuel_cost DECIMAL(10,2),                      -- fuel cost for the flight
    co2_per_flight DECIMAL(10,2),                 -- CO2 produced per flight
    passengers INT,                               -- number of passengers
    ticket_price DECIMAL(10,2) DEFAULT 200.00    -- price per ticket
);


CREATE TABLE flight_logs (
    flight_id VARCHAR(50) PRIMARY KEY,            -- unique ID for each flight
    userid INT,                                   -- references the user who flew
    routeid CHAR(3),                              -- references the route flown
    profit_generated DECIMAL(12,2),               -- profit from this flight
    co2_produced DECIMAL(12,2),                   -- CO2 produced in this flight
    flight_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- time of the flight
    FOREIGN KEY (userid) REFERENCES users(userid),
    FOREIGN KEY (routeid) REFERENCES routes(routeid)
);

CREATE TABLE investments (
    investmentid VARCHAR(20) PRIMARY KEY,        -- unique investment ID
    userid INT,                                  -- references the user who invested
    amount INT,                                  -- amount invested
    co2_reduced INT,                             -- CO2 reduction achieved
    reputation_increased INT,                    -- reputation gained
    investment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- time of investment
    FOREIGN KEY (userid) REFERENCES users(userid)
);

SET SQL_SAFE_UPDATES = 0;
-- ( generating values for passengers column randomly between 100 to 300  ) FLOOR(MIN + RAND() * (MAX - MIN + 1))
-- -- UPDATE routes 
-- SET passengers = FLOOR(100 + (RAND() * 201))

-- ALTER TABLE routes 
-- ADD COLUMN ticket_price DECIMAL(10,2) NOT NULL DEFAULT 200.00;

-- SET SQL_SAFE_UPDATES = 0;
-- ( generating values for ticket_price column randomly between 100 to 500  ) FLOOR(MIN + RAND() * (MAX - MIN + 1))
-- UPDATE routes 
-- SET ticket_price = ROUND(100 + (RAND() * 401), 2);

INSERT INTO `routes` VALUES
('AER','Sochi International Airport',43.449902,39.956600,'Sochi',465.15,NULL,NULL,144,482.42),
('ALC','Alicante-Elche Miguel HernÃƒÂ¡ndez Airport',38.282200,-0.558156,'Alicante',120.23,NULL,NULL,191,400.21),
('AMS','Amsterdam Airport Schiphol',52.308601,4.763890,'Amsterdam',55.7,NULL,NULL,222,353.77),
('ARN','Stockholm-Arlanda Airport',59.651901,17.918600,'Stockholm',317.79,NULL,NULL,238,368.25),
('ATH','Athens Eleftherios Venizelos International Airport',37.936401,23.944500,'Athens',471.86,NULL,NULL,224,279.93),
('BCN','Josep Tarradellas Barcelona-El Prat Airport',41.297100,2.078460,'Barcelona',455.95,NULL,NULL,107,394.89),
('BEG','Belgrade Nikola Tesla Airport',44.818401,20.309099,'Belgrade',364.16,NULL,NULL,163,334.66),
('BER','Berlin Brandenburg Airport',52.351389,13.493889,'Berlin',402.93,NULL,NULL,193,288.62),
('BFS','Belfast International Airport',54.657501,-6.215830,'Belfast',422.17,NULL,NULL,177,239.14),
('BGO','Bergen Airport, Flesland',60.293400,5.218140,'Bergen',402.08,NULL,NULL,207,429.85),
('BGY','Milan Bergamo Airport',45.673901,9.704170,'Milan',243.88,NULL,NULL,205,331.82),
('BHX','Birmingham International Airport',52.453899,-1.748030,'Birmingham',413.15,NULL,NULL,100,469.55),
('BLL','Billund Airport',55.740299,9.151780,'Billund',384.13,NULL,NULL,190,252.28),
('BLQ','Bologna Guglielmo Marconi Airport',44.535400,11.288700,'Bologna',181.2,NULL,NULL,149,252.77),
('BOJ','Burgas Airport',42.569599,27.515200,'Burgas',153.59,NULL,NULL,276,307.00),
('BRU','Brussels Airport',50.901402,4.484440,'Brussels',174.38,NULL,NULL,228,276.67),
('BUD','Budapest Liszt Ferenc International Airport',47.429760,19.261093,'Budapest',361.1,NULL,NULL,216,262.38),
('CAG','Cagliari Elmas Airport',39.251499,9.054280,'Cagliari',332.36,NULL,NULL,295,281.88),
('CDG','Charles de Gaulle International Airport',49.012798,2.550000,'Paris',78.52,NULL,NULL,123,422.26),
('CGN','Cologne Bonn Airport',50.865898,7.142740,'Cologne',245.53,NULL,NULL,234,465.66),
('CPH','Copenhagen Kastrup Airport',55.617901,12.656000,'Copenhagen',492.07,NULL,NULL,299,261.52),
('CTA','Catania-Fontanarossa Airport',37.466801,15.066400,'Catania',323.78,NULL,NULL,294,310.63),
('DME','Domodedovo International Airport',55.408798,37.906300,'Moscow',92.68,NULL,NULL,271,268.60),
('DUB','Dublin Airport',53.421299,-6.270070,'Dublin',342.06,NULL,NULL,173,211.08),
('EDI','Edinburgh Airport',55.950145,-3.372288,'Edinburgh',482.24,NULL,NULL,151,349.62),
('EIN','Eindhoven Airport',51.450100,5.374530,'Eindhoven',435.05,NULL,NULL,140,314.85),
('FRA','Frankfurt am Main Airport',50.036249,8.559294,'Frankfurt am Main',228.5,NULL,NULL,145,325.39),
('FUE','Fuerteventura Airport',28.452700,-13.863800,'Fuerteventura Island',237.37,NULL,NULL,205,482.40),
('GLA','Glasgow International Airport',55.871899,-4.433060,'Paisley, Renfrewshire',451.34,NULL,NULL,291,335.82),
('GOT','Gothenburg-Landvetter Airport',57.662800,12.279800,'Gothenburg',144.6,NULL,NULL,136,331.89),
('GRV','Grozny North Airport',43.388302,45.698601,'Grozny',218.99,NULL,NULL,109,451.99),
('GSV','Gagarin International Airport',51.712778,46.171111,'Saratov',161.12,NULL,NULL,239,464.28),
('GVA','Geneva Cointrin International Airport',46.238098,6.108950,'Geneva',98.66,NULL,NULL,168,465.44),
('HAJ','Hannover Airport',52.461102,9.685080,'Hannover',409.93,NULL,NULL,222,434.37),
('HAM','Hamburg Helmut Schmidt Airport',53.630402,9.988230,'Hamburg',353.68,NULL,NULL,106,275.53),
('HEL','Helsinki Vantaa Airport',60.317200,24.963301,'Helsinki',488.59,NULL,NULL,165,474.54),
('HER','Heraklion International Nikos Kazantzakis Airport',35.339699,25.180300,'Heraklion',431.92,NULL,NULL,208,446.12),
('IBZ','Ibiza Airport',38.872898,1.373120,'Ibiza',193.83,NULL,NULL,242,306.96),
('KBP','Boryspil International Airport',50.345001,30.894699,'Kiev',73.37,NULL,NULL,287,296.44),
('KJA','Krasnoyarsk International Airport',56.173077,92.492437,'Krasnoyarsk',185.39,NULL,NULL,208,361.31),
('KUF','Kurumoch International Airport',53.504902,50.164299,'Samara',206.81,NULL,NULL,280,417.23),
('KZN','Kazan International Airport',55.606201,49.278702,'Kazan',427.91,NULL,NULL,273,202.22),
('LED','Pulkovo Airport',59.800301,30.262501,'St. Petersburg',119.1,NULL,NULL,227,459.41),
('LEJ','Leipzig/Halle Airport',51.423889,12.236389,'Leipzig',161.78,NULL,NULL,215,290.39),
('LGW','London Gatwick Airport',51.148102,-0.190278,'London',401.58,NULL,NULL,295,473.74),
('LHR','London Heathrow Airport',51.470600,-0.461941,'London',122.57,NULL,NULL,126,397.52),
('LIS','Humberto Delgado Airport (Lisbon Portela Airport)',38.781300,-9.135920,'Lisbon',258.13,NULL,NULL,248,366.36),
('LPA','Gran Canaria Airport',27.931900,-15.386600,'Gran Canaria Island',422.94,NULL,NULL,161,439.27),
('LTN','London Luton Airport',51.874699,-0.368333,'London',390.29,NULL,NULL,163,297.26),
('LUX','Luxembourg-Findel International Airport',49.623333,6.204444,'Luxembourg',182.63,NULL,NULL,233,268.48),
('LWO','Lviv International Airport',49.812500,23.956100,'Lviv',142.27,NULL,NULL,173,250.64),
('LYS','Lyon Saint-ExupÃƒÂ©ry Airport',45.725556,5.081111,'Lyon',113.46,NULL,NULL,267,247.77),
('MAN','Manchester Airport',53.349375,-2.279521,'Manchester',90.51,NULL,NULL,114,286.92),
('MLA','Malta International Airport',35.857498,14.477500,'Valletta',62.18,NULL,NULL,271,491.30),
('MRS','Marseille Provence Airport',43.439272,5.221424,'Marseille',439.35,NULL,NULL,110,495.75),
('MSQ','Minsk National Airport',53.888071,28.039964,'Minsk',160.21,NULL,NULL,241,204.83),
('MUC','Munich Airport',48.353802,11.786100,'Munich',332.98,NULL,NULL,173,236.91),
('MXP','Malpensa International Airport',45.630600,8.728110,'Milan',234.3,NULL,NULL,245,370.07),
('NAP','Naples International Airport',40.886002,14.290800,'NÃƒÂ¡poli',122.54,NULL,NULL,202,339.62),
('NUE','Nuremberg Airport',49.498699,11.078056,'Nuremberg',309.81,NULL,NULL,178,387.88),
('ORY','Paris-Orly Airport',48.723333,2.379444,'Paris',231.43,NULL,NULL,182,420.54),
('OSL','Oslo Airport, Gardermoen',60.193901,11.100400,'Oslo',177.74,NULL,NULL,277,439.07),
('OVB','Novosibirsk Tolmachevo Airport',55.019756,82.618675,'Novosibirsk',144.37,NULL,NULL,138,433.73),
('PMI','Palma de Mallorca Airport',39.551701,2.738810,'Palma De Mallorca',138.67,NULL,NULL,162,351.45),
('PSA','Pisa International Airport',43.683899,10.392700,'Pisa',210.22,NULL,NULL,296,256.06),
('RIX','Riga International Airport',56.923599,23.971100,'Riga',135.09,NULL,NULL,289,325.94),
('ROV','Platov International Airport',47.493888,39.924722,'Rostov-on-Don',444.79,NULL,NULL,260,361.52),
('SCQ','Santiago-RosalÃƒÂ­a de Castro Airport',42.896301,-8.415140,'Santiago de Compostela',418.69,NULL,NULL,130,329.76),
('SKG','Thessaloniki Macedonia International Airport',40.519699,22.970900,'Thessaloniki',259.06,NULL,NULL,172,364.26),
('SKP','Skopje International Airport',41.961601,21.621401,'Skopje',439.23,NULL,NULL,171,332.00),
('SOF','Sofia Airport',42.696693,23.411436,'Sofia',469,NULL,NULL,238,367.23),
('STN','London Stansted Airport',51.884998,0.235000,'London',77.28,NULL,NULL,177,340.16),
('STR','Stuttgart Airport',48.689899,9.221960,'Stuttgart',279.4,NULL,NULL,271,399.11),
('SVG','Stavanger Airport, Sola',58.876701,5.637780,'Stavanger',215.15,NULL,NULL,124,475.06),
('SVO','Sheremetyevo International Airport',55.972599,37.414600,'Moscow',187.56,NULL,NULL,108,377.97),
('TFS','Tenerife Sur Airport',28.044500,-16.572500,'Tenerife',242.34,NULL,NULL,269,264.65),
('TGD','Podgorica Airport / Podgorica Golubovci Airbase',42.359402,19.251900,'Podgorica',149.03,NULL,NULL,117,289.37),
('TIA','Tirana International Airport Mother Teresa',41.414700,19.720600,'Tirana',418.13,NULL,NULL,283,452.87),
('TLL','Lennart Meri Tallinn Airport',59.413300,24.832800,'Tallinn',243.57,NULL,NULL,158,296.26),
('TLS','Toulouse-Blagnac Airport',43.629101,1.363820,'Toulouse/Blagnac',363.43,NULL,NULL,247,222.69),
('TRN','Turin Airport',45.200802,7.649630,'Torino',136.47,NULL,NULL,257,324.68),
('UFA','Ufa International Airport',54.557499,55.874401,'Ufa',442.03,NULL,NULL,244,455.32),
('VAR','Varna Airport',43.232101,27.825100,'Varna',400.77,NULL,NULL,147,202.54),
('VCE','Venice Marco Polo Airport',45.505299,12.351900,'Venice',177.76,NULL,NULL,108,346.75),
('VIE','Vienna International Airport',48.110298,16.569700,'Vienna',86.5,NULL,NULL,197,326.15),
('VKO','Vnukovo International Airport',55.591499,37.261501,'Moscow',299.2,NULL,NULL,162,390.47),
('VNO','Vilnius International Airport',54.634102,25.285801,'Vilnius',286.5,NULL,NULL,119,473.91),
('VRN','Verona Villafranca Airport',45.395699,10.888500,'Verona',484.9,NULL,NULL,209,398.15),
('VVO','Vladivostok International Airport',43.396256,132.148155,'Artyom',165.02,NULL,NULL,185,368.99),
('WAW','Warsaw Chopin Airport',52.165699,20.967100,'Warsaw',220.38,NULL,NULL,202,450.53),
('ZIA','Zhukovsky International Airport',55.553299,38.150002,'Moscow',106.84,NULL,NULL,152,345.67);



ALTER TABLE routes
MODIFY airport_fee FLOAT DEFAULT 0;

--ALTER TABLE routes ADD COLUMN ticket_price DECIMAL(10,2);
--select * FROM routes;

ALTER TABLE investments
MODIFY investmentid VARCHAR(20);

ALTER TABLE investments
MODIFY investmentid VARCHAR(20) PRIMARY KEY;

ALTER TABLE flight_logs
DROP PRIMARY KEY;

ALTER TABLE flight_logs
MODIFY flight_id VARCHAR(50) NOT NULL PRIMARY KEY;

UPDATE routes
SET airport_fee = ROUND(50 + (RAND() * (500 - 50)), 2)

