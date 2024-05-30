'Normalization

Your queries should be executable on MySQL.

The initial supermarket table as mentioned in the question is as follows:

db

However, as it is clear, the design of this database is not optimal and it has data redundancy.

In this question, we ask you to normalize this database.

Project Details

The information of the existing table is as follows:

Column Name	Type	Definition
m_id	bigint AUTO_INCREMENT	Branch ID
m_name	varchar(255)	Branch Name
m_address	text	Branch Address
p_id	bigint AUTO_INCREMENT	Product ID
p_name	varchar(255)	Product Name
p_weight	bigint	Product Weight
price	bigint	Product Price
level	int	Branch Level
m_score	bigint	Branch Score
capacity	bigint	Capacity of the number of products related to the branch level
Also note that in the above table, m_id and p_id are keys.

Requirements

The only requirement in this question is to create the normalized version of the table mentioned at the beginning of the question using only DDL commands.

You should continue normalization until none of the dependencies are violated.

Important Note

You should use the table names as per the following table:

Key	Table Name
Branches	markets
Scores	scores
Products	products
Names	names
Weights	weights
Addresses	addresses
Prices	prices
Capacities	capacities
Notes

You do not need to use all the tables mentioned in the above table, and you should only use the tables you need.
All column information (such as names, etc.) should be similar to the ones mentioned at the beginning of the question and should not be changed.
NULL values are not allowed in any of the columns.
Foreign keys should be correctly created (their names do not matter).
What to Upload
After designing the queries, upload your code as a file with the .sql extension.'


create database if not exists market_products;

use market_products;
                        
create table if not exists capacities
					    (level int not null primary key,
                         capacity bigint not null
                         );
                        
create table if not exists markets 
						(m_id bigint primary key auto_increment not null,
						 m_name varchar(255) not null,
                         m_address text not null,
                         level int not null,
                         m_score bigint not null,
                         foreign key(level) references capacities(level)
                        );
                      
create table if not exists products 
					   (p_id bigint primary key auto_increment not null,
						p_name varchar(255) not null,
                        p_weight bigint not null);
                        
create table if not exists prices 
						(
						 m_id bigint not null,
						 p_id bigint not null,
						 price bigint not null,
						 primary key (m_id, p_id),
						 foreign key (m_id) references markets(m_id),
						 foreign key (p_id) references products(p_id)
						 );
