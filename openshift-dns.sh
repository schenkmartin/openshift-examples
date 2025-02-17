#!/bin/bash
sudo resolvectl domain crc ~testing;
sudo resolvectl dns crc 192.168.130.11;
sudo resolvectl llmnr crc yes

