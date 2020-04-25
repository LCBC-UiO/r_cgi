# R cgi

Example CGI scripts in R

## Quick start

  * `git clone ... && cd ...`
  * `PORT=8080 make run`
  * open browser and go to `http://localhost:8080`

## Requirements

  * Linux / Mac OS
  * build tools (make, gcc, ...)
  * Rscript in PATH

## Examples

  *  Simple plot
  *  Plot with parameters
  *  Plot with parameters and dynamic update
  *  File upload
  *  File upload with parameters

### Running examples CGIs from command line

```
www/plot/get_plot_png.cgi > /tmp/plot.png
QUERY_STRING='width=300&height=300' www/plot_param/get_plot_png.cgi > /tmp/plot.png
cat test_table.csv | www/post/post_file.cgi
cat test_table.csv | QUERY_STRING='filename=/tmp/test123.csv' www/post_param/post_file.cgi
```
