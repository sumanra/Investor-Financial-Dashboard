-- DROP DATABASE `stockml_db`
DROP DATABASE `stockml_db`;

-- Create and use stockml_db
CREATE DATABASE stockml_db;
USE stockml_db;

-- Create tables for raw data to be loaded into database

-- 	dates	open	high	low	close	adjusted close	volume	dividend amount	tickers
-- Creating table for Citizens Financial Group (ticker: CFG)  
CREATE TABLE cfg_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);

select * from cfg_profile;

-- Creating table for Morgan Stanley (ticker: MS)
CREATE TABLE ms_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);

select * from ms_profile;

-- Creating table for CME Group (ticker: CME)

CREATE TABLE cme_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);

select * from cme_profile;

-- Creating table for JPMorgan Chase & Co. (ticker: JPM)
CREATE TABLE jpm_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);

select * from jpm_profile;

CREATE TABLE gs_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);

select * from gs_profile;

CREATE TABLE pypl_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);

select * from pypl_profile;

CREATE TABLE brka_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);
select * from brka_profile;

CREATE TABLE brkb_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);
select * from brkb_profile;

CREATE TABLE usb_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);
select * from usb_profile;

CREATE TABLE ibkr_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);
select * from ibkr_profile;

CREATE TABLE axp_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);
select * from axp_profile;

CREATE TABLE Stocks_profile (
  id INT primary key auto_increment ,
  dates date,
  open float,
  high float,
  low float,
  close float,
  adjusted_close float,
  volume float,
  ticker Text
);
select * from Stocks_profile;