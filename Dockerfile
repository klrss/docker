FROM ubuntu:16.04
RUN apt-get -y update && apt-get -y install apache2
RUN echo 'ServerName localhost'>> /etc/apache2/apache2.conf
RUN echo 'Hi there, what is love? \n It is just a song...'>/var/www/html/index.html
CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]
EXPOSE 80

