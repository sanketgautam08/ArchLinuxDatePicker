#!/bin/sh

# konsole  -e pip install tk tkcalendar
# konsole --noclose -e echo "Downloading tk" && sudo pacman -S tk
{
echo "Installing TKinter and tkcalendar"
sudo pacman -S python-pip
pip install tk tkcalendar
echo "Downloading tk"
sudo pacman -S tk
echo "Setup Complete. Execute 'run.sh' to run the program."
echo "Press any ENTER to exit."
read key
}

