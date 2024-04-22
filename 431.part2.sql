create table data (recordId int primary key, agencyCode varchar(255), 
				   agencyName varchar(255), agencyType varchar(255), 
				   city varchar(255), states varchar(255), years varchar(255), 
				   months varchar(255), incident varchar(255), crimeType varchar(255), 
				   crimeSolved varchar(255), victimSex varchar(255), victimAge varchar(255), 
				   victimRace varchar(255), victimEthnicity varchar(255), 
				  perpetratorSex varchar(255), perpetratorAge varchar(255), 
				   perpetratorRace varchar(255), perpetratorEthnicity varchar(255),
				   relationship varchar(255), weapon varchar(255), victimCount varchar(255), perpetratorCount varchar(255));

copy data
from 'C:\Users\Public\database(AutoRecovered).csv'
delimiter ','
csv header;

CREATE TABLE agency AS 
SELECT DISTINCT on (agencyCode)
agencyCode, agencyName, agencyType, city
FROM data;

CREATE TABLE perpetrators AS
SELECT recordId, perpetratorSex, perpetratorAge, perpetratorRace, perpetratorEthnicity, perpetratorCount
FROM data;

ALTER TABLE perpetrators
ADD PRIMARY KEY(recordId);

CREATE TABLE crime AS
SELECT recordId, agencyCode, crimeType, relationship,weapon,months,years
FROM data;

ALTER TABLE crime
ADD PRIMARY KEY(recordId);

CREATE TABLE victim AS
SELECT recordId, victimSex, victimAge, victimRace, victimEthnicity, victimCount
FROM data;

ALTER TABLE victim
ADD PRIMARY KEY(recordId);

CREATE TABLE locations AS
SELECT DISTINCT on (city)
city,states,incident
FROM data;