
<!-- rnb-text-begin -->

---
title: "GAEZ Hyper-localization"
output: html_notebook
---

Steps to create R projects:
1.	Navigate to directory that will host the project folder.
2.	In R, load ‘rrtools’ and ‘workflowr’
3.	Run ‘rrtools’ code to create research compendium:
a.	rrtools::use_compendium("myproject ")
b.	usethis::use_mit_license(name = "Jonathan J Maynard")
c.	usethis::use_git()
d.	Create github ‘repo’ token for “myproject”: gitcreds::gitcreds_set() -- set new token created on GitHub website
e.	usethis::use_github()
f.	rrtools::use_readme_rmd()
g.	rrtools::use_analysis()
h.	rename the ‘analysis’ folder to ‘report’
i.	rrtools::use_dockerfile()
j.	rrtools::use_travis()
4.	Run ‘workflowr’ code to create research website
a.	wflow_start("myproject_site")
b.	wflow_build() and wflow_view() to build and view website
c.	wflow_publish(c("analysis/index.Rmd", "analysis/about.Rmd", "analysis/license.Rmd"), "Publish the initial files for myproject")
d.	wflow_status() to check if docs have been published
5.	Integreate rrtools folder and workflow folder:
a.	Move items from "myproject_site" to "myproject "
6.	Commit changes with Git and push to GitHub. All future changes can be pushed to

# Modify this section for each new project

<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxuYGBgclxuIyBzZXQgcHJvamVjdCBuYW1lIGFuZCBwYXRoXG5uYW1lIDwtIFxcR0FFWlxcXG5wYXRoIDwtIFxcQzovUl9Ecml2ZS9EYXRhX0ZpbGVzL0xQS1NfRGF0YS9SX1Byb2plY3RzL0dBRVpcXFxuYGBgXG5gYGBcbmBgYCJ9 -->

```r
```r
```r
# set project name and path
name <- \GAEZ\
path <- \C:/R_Drive/Data_Files/LPKS_Data/R_Projects/GAEZ\
```
```
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxubGlicmFyeShycnRvb2xzKVxuYGBgXG5gYGAifQ== -->

```r
```r
library(rrtools)
```
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiXHUwMDFiWzMybTxVKzI3MTQ+XHUwMDFiWzM5bSBHaXQgaXMgaW5zdGFsbGVkIG9uIHRoaXMgY29tcHV0ZXIsIHlvdXIgdXNlcm5hbWUgaXMgXHUwMDFiWzMybWpqbWF5bmFyZFx1MDAxYlszOW1cbiJ9 -->

```
[32m<U+2714>[39m Git is installed on this computer, your username is [32mjjmaynard[39m
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxubGlicmFyeSh3b3JrZmxvd3IpXG5gYGBcbmBgYCJ9 -->

```r
```r
library(workflowr)
```
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiVGhpcyBpcyB3b3JrZmxvd3IgdmVyc2lvbiAxLjYuMlxuUnVuID93b3JrZmxvd3IgZm9yIGhlbHAgZ2V0dGluZyBzdGFydGVkXG4ifQ== -->

```
This is workflowr version 1.6.2
Run ?workflowr for help getting started
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxudXNldGhpczo6dXNlX21pdF9saWNlbnNlKGNvcHlyaWdodF9ob2xkZXIgPSBcXEpvbmF0aGFuIEogTWF5bmFyZFxcKVxuXG5gYGBcbmBgYCJ9 -->

```r
```r
usethis::use_mit_license(copyright_holder = \Jonathan J Maynard\)

```
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiXHUwMDFiWzMybXZcdTAwMWJbMzltIFdyaXRpbmcgXHUwMDFiWzM0bSdMSUNFTlNFJ1x1MDAxYlszOW1cblx1MDAxYlszMm12XHUwMDFiWzM5bSBXcml0aW5nIFx1MDAxYlszNG0nTElDRU5TRS5tZCdcdTAwMWJbMzltXG5cdTAwMWJbMzJtdlx1MDAxYlszOW0gQWRkaW5nIFx1MDAxYlszNG0nXkxJQ0VOU0VcXFxcLm1kJCdcdTAwMWJbMzltIHRvIFx1MDAxYlszNG0nLlJidWlsZGlnbm9yZSdcdTAwMWJbMzltXG4ifQ== -->

```
[32mv[39m Writing [34m'LICENSE'[39m
[32mv[39m Writing [34m'LICENSE.md'[39m
[32mv[39m Adding [34m'^LICENSE\\.md$'[39m to [34m'.Rbuildignore'[39m
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->


# Add auth_token for project


<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuIyBzZXQgdG9rZW4gaW4gc3RvcmFnZVxuI1Rva2VuIGZvciBHQUVaIEh5cGVybG9jYWxpemF0aW9uOiBcImdocF90SU85OGNmN2M4YTdCTGhlMk5pYVN4b28yRDdYMDExbDhMcDZcIlxuZ2l0Y3JlZHM6OmdpdGNyZWRzX3NldCgpXG5cbmBgYCJ9 -->

```r
# set token in storage
#Token for GAEZ Hyperlocalization: "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"
gitcreds::gitcreds_set()

```

<!-- rnb-source-end -->



<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuZ2hwX2RhZ24zdU9yUzFnRGxrMkZwSjZMV0F0VkZRaEhKMDBJZkxValxuYGBgIn0= -->

```r
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
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiLT4gQWRkaW5nIG5ldyBjcmVkZW50aWFscy4uLlxuLT4gUmVtb3ZpbmcgY3JlZGV0aWFscyBmcm9tIGNhY2hlLi4uXG4tPiBEb25lLlxuIn0= -->

```
-> Adding new credentials...
-> Removing credetials from cache...
-> Done.
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->


# Run workflowr code as chunk

<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxuc2V0d2Qod2Zscl9wYXRoKVxuYGBgXG5gYGAifQ== -->

```r
```r
setwd(wflr_path)
```
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiVGhlIHdvcmtpbmcgZGlyZWN0b3J5IHdhcyBjaGFuZ2VkIHRvIEM6L1JfRHJpdmUvRGF0YV9GaWxlcy9MUEtTX0RhdGEvUl9Qcm9qZWN0cy9HQUVaL0dBRVpfc2l0ZSBpbnNpZGUgYSBub3RlYm9vayBjaHVuay4gVGhlIHdvcmtpbmcgZGlyZWN0b3J5IHdpbGwgYmUgcmVzZXQgd2hlbiB0aGUgY2h1bmsgaXMgZmluaXNoZWQgcnVubmluZy4gVXNlIHRoZSBrbml0ciByb290LmRpciBvcHRpb24gaW4gdGhlIHNldHVwIGNodW5rIHRvIGNoYW5nZSB0aGUgd29ya2luZyBkaXJlY3RvcnkgZm9yIG5vdGVib29rIGNodW5rcy5cbiJ9 -->

```
The working directory was changed to C:/R_Drive/Data_Files/LPKS_Data/R_Projects/GAEZ/GAEZ_site inside a notebook chunk. The working directory will be reset when the chunk is finished running. Use the knitr root.dir option in the setup chunk to change the working directory for notebook chunks.
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxud2Zsb3dfcHVibGlzaChjKFxcc2l0ZS9pbmRleC5SbWRcXCwgXFxzaXRlL2NvZGUuUm1kXFwsIFxcc2l0ZS9kYXRhLlJtZFxcLCBcXHNpdGUvbGljZW5zZS5SbWRcXCksIFxcUHVibGlzaCB0aGUgaW5pdGlhbCBmaWxlcyBmb3IgbXlwcm9qZWN0XFwpXG5gYGBcbmBgYCJ9 -->

```r
```r
wflow_publish(c(\site/index.Rmd\, \site/code.Rmd\, \site/data.Rmd\, \site/license.Rmd\), \Publish the initial files for myproject\)
```
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiVGhlIGZvbGxvd2luZyBSIE1hcmtkb3duIGZpbGUocykgaGF2ZSBub3QgYmVlbiBjb21taXR0ZWQgdG8gdGhlIEdpdCByZXBvc2l0b3J5IGJ1dCB0aGVpclxuY29ycmVzcG9uZGluZyBIVE1MIGZpbGUocykgaGF2ZS4gVGhpcyB2aW9sYXRlcyB0aGUgcmVwcm9kdWNpYmlsaXR5IGd1YXJhbnRlZSBvZlxud29ya2Zsb3dyLiBQbGVhc2UgcHVibGlzaCB0aGVzZSBmaWxlcyB1c2luZyB3Zmxvd19wdWJsaXNoKCkgdG8gZml4IHRoaXMgc2l0dWF0aW9uLlxuXG5zaXRlL2NvZGUuUm1kXG5zaXRlL2RhdGEuUm1kXG5zaXRlL2luZGV4LlJtZFxuc2l0ZS9saWNlbnNlLlJtZEN1cnJlbnQgd29ya2luZyBkaXJlY3Rvcnk6IEM6L1JfRHJpdmUvRGF0YV9GaWxlcy9MUEtTX0RhdGEvUl9Qcm9qZWN0cy9HQUVaL0dBRVpfc2l0ZVxuQnVpbGRpbmcgNCBmaWxlKHMpOlxuQnVpbGRpbmcgc2l0ZS9pbmRleC5SbWRcbkJ1aWxkaW5nIHNpdGUvY29kZS5SbWRcbkJ1aWxkaW5nIHNpdGUvZGF0YS5SbWRcbkJ1aWxkaW5nIHNpdGUvbGljZW5zZS5SbWRcblN1bW1hcnkgZnJvbSB3Zmxvd19wdWJsaXNoXG5cbioqU3RlcCAxOiBDb21taXQgYW5hbHlzaXMgZmlsZXMqKlxuXG5ObyBmaWxlcyB0byBjb21taXRcblxuXG4qKlN0ZXAgMjogQnVpbGQgSFRNTCBmaWxlcyoqXG5cblN1bW1hcnkgZnJvbSB3Zmxvd19idWlsZFxuXG5TZXR0aW5nczpcbiBjbGVhbl9maWdfZmlsZXM6IFRSVUVcblxuVGhlIGZvbGxvd2luZyB3ZXJlIGJ1aWx0IGV4dGVybmFsbHkgZWFjaCBpbiB0aGVpciBvd24gZnJlc2ggUiBzZXNzaW9uOiBcblxuZG9jcy9pbmRleC5odG1sXG5kb2NzL2NvZGUuaHRtbFxuZG9jcy9kYXRhLmh0bWxcbmRvY3MvbGljZW5zZS5odG1sXG5cbkxvZyBmaWxlcyBzYXZlZCBpbiBDOlxcVXNlcnNcXGptYXluYXJkXFxBcHBEYXRhXFxMb2NhbFxcVGVtcFxcUnRtcElyYmtCTy93b3JrZmxvd3JcblxuKipTdGVwIDM6IENvbW1pdCBIVE1MIGZpbGVzKipcblxuU3VtbWFyeSBmcm9tIHdmbG93X2dpdF9jb21taXRcblxuVGhlIGZvbGxvd2luZyB3YXMgcnVuOiBcblxuICAkIGdpdCBhZGQgZG9jcy9pbmRleC5odG1sIGRvY3MvY29kZS5odG1sIGRvY3MvZGF0YS5odG1sIGRvY3MvbGljZW5zZS5odG1sIGRvY3MvZmlndXJlL2luZGV4LlJtZCBkb2NzL2ZpZ3VyZS9jb2RlLlJtZCBkb2NzL2ZpZ3VyZS9kYXRhLlJtZCBkb2NzL2ZpZ3VyZS9saWNlbnNlLlJtZCBkb2NzL3NpdGVfbGlicyBkb2NzLy5ub2pla3lsbCBcbiAgJCBnaXQgY29tbWl0IC1tIFxcQnVpbGQgc2l0ZS5cXCBcblxuVGhlIGZvbGxvd2luZyBmaWxlKHMpIHdlcmUgaW5jbHVkZWQgaW4gY29tbWl0IGNiNGYyOWQ6XG5kb2NzL2NvZGUuaHRtbFxuZG9jcy9kYXRhLmh0bWxcbmRvY3MvaW5kZXguaHRtbFxuZG9jcy9saWNlbnNlLmh0bWxcbiJ9 -->

```
The following R Markdown file(s) have not been committed to the Git repository but their
corresponding HTML file(s) have. This violates the reproducibility guarantee of
workflowr. Please publish these files using wflow_publish() to fix this situation.

site/code.Rmd
site/data.Rmd
site/index.Rmd
site/license.RmdCurrent working directory: C:/R_Drive/Data_Files/LPKS_Data/R_Projects/GAEZ/GAEZ_site
Building 4 file(s):
Building site/index.Rmd
Building site/code.Rmd
Building site/data.Rmd
Building site/license.Rmd
Summary from wflow_publish

**Step 1: Commit analysis files**

No files to commit


**Step 2: Build HTML files**

Summary from wflow_build

Settings:
 clean_fig_files: TRUE

The following were built externally each in their own fresh R session: 

docs/index.html
docs/code.html
docs/data.html
docs/license.html

Log files saved in C:\Users\jmaynard\AppData\Local\Temp\RtmpIrbkBO/workflowr

**Step 3: Commit HTML files**

Summary from wflow_git_commit

The following was run: 

  $ git add docs/index.html docs/code.html docs/data.html docs/license.html docs/figure/index.Rmd docs/figure/code.Rmd docs/figure/data.Rmd docs/figure/license.Rmd docs/site_libs docs/.nojekyll 
  $ git commit -m \Build site.\ 

The following file(s) were included in commit cb4f29d:
docs/code.html
docs/data.html
docs/index.html
docs/license.html
```



<!-- rnb-output-end -->

<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxud2Zsb3dfc3RhdHVzKCkgI3RvIGNoZWNrIGlmIGRvY3MgaGF2ZSBiZWVuIHB1Ymxpc2hlZFxuYGBgXG5gYGAifQ== -->

```r
```r
wflow_status() #to check if docs have been published
```
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiVGhlIGZvbGxvd2luZyBSIE1hcmtkb3duIGZpbGUocykgaGF2ZSBub3QgYmVlbiBjb21taXR0ZWQgdG8gdGhlIEdpdCByZXBvc2l0b3J5IGJ1dCB0aGVpclxuY29ycmVzcG9uZGluZyBIVE1MIGZpbGUocykgaGF2ZS4gVGhpcyB2aW9sYXRlcyB0aGUgcmVwcm9kdWNpYmlsaXR5IGd1YXJhbnRlZSBvZlxud29ya2Zsb3dyLiBQbGVhc2UgcHVibGlzaCB0aGVzZSBmaWxlcyB1c2luZyB3Zmxvd19wdWJsaXNoKCkgdG8gZml4IHRoaXMgc2l0dWF0aW9uLlxuXG5zaXRlL2NvZGUuUm1kXG5zaXRlL2RhdGEuUm1kXG5zaXRlL2luZGV4LlJtZFxuc2l0ZS9saWNlbnNlLlJtZFxuU3RhdHVzIG9mIDQgUm1kIGZpbGVzXG5cblRvdGFsczpcbiA0IFVucHVibGlzaGVkXG5cblRoZSBmb2xsb3dpbmcgUm1kIGZpbGVzIHJlcXVpcmUgYXR0ZW50aW9uOlxuXG5VbnAgc2l0ZS9jb2RlLlJtZFxuVW5wIHNpdGUvZGF0YS5SbWRcblVucCBzaXRlL2luZGV4LlJtZFxuVW5wIHNpdGUvbGljZW5zZS5SbWRcblxuS2V5OiBVbnAgPSBVbnB1Ymxpc2hlZFxuXG5UaGUgY3VycmVudCBHaXQgc3RhdHVzIGlzOlxuXG5cblRvIHB1Ymxpc2ggeW91ciBjaGFuZ2VzIGFzIHBhcnQgb2YgeW91ciB3ZWJzaXRlLCB1c2UgYHdmbG93X3B1Ymxpc2goKWAuXG5UbyBjb21taXQgeW91ciBjaGFuZ2VzIHdpdGhvdXQgcHVibGlzaGluZyB0aGVtIHlldCwgdXNlIGB3Zmxvd19naXRfY29tbWl0KClgLlxuXG5UaGUgY29uZmlnIGZpbGUgX3dvcmtmbG93ci55bWwgaGFzIGJlZW4gZWRpdGVkLlxuIn0= -->

```
The following R Markdown file(s) have not been committed to the Git repository but their
corresponding HTML file(s) have. This violates the reproducibility guarantee of
workflowr. Please publish these files using wflow_publish() to fix this situation.

site/code.Rmd
site/data.Rmd
site/index.Rmd
site/license.Rmd
Status of 4 Rmd files

Totals:
 4 Unpublished

The following Rmd files require attention:

Unp site/code.Rmd
Unp site/data.Rmd
Unp site/index.Rmd
Unp site/license.Rmd

Key: Unp = Unpublished

The current Git status is:


To publish your changes as part of your website, use `wflow_publish()`.
To commit your changes without publishing them yet, use `wflow_git_commit()`.

The config file _workflowr.yml has been edited.
```



<!-- rnb-output-end -->

<!-- rnb-frame-begin eyJtZXRhZGF0YSI6eyJjbGFzc2VzIjoiZGF0YS5mcmFtZSIsIm5jb2wiOjMsIm5yb3ciOjIxfSwicmRmIjoiSDRzSUFBQUFBQUFBQnUyVVQwL2JNQlRBVFpxd0pWc0xBdlhHWVY4QVR6RHRBN0NtUWoxUVVGWWt0RXZsSkc0eFRlektzVlc0OGNrWno2bmR0SmwyWUpmdHNFaVc3ZC83LzE3a0pMNzdFdDFGQ0tFTzhwR0hPZ0VjMGY3ZzV1ejg2emxDdmdlM1BaQ0VabjhFcmVOYUZhRkRXSDByZUs5NXBjaWM1bjk0RHpWWGttU0wvK0FYMEdwMEtYSTJZMDBqMzNqLysvWDhzMkMzMFljWWY4WkpxbG1Sc3prWGtscmVBeDRQdncrUzBjMWtkRDIyOUFUbzVjWHd4M1FweFFQTjFEU1RsQ2dtT0U1S0YrclRiM1Y0aXU5VldWaTlMdWdOcnNmeDdXQ0NOOFpIYXpoSlJ0OXVKNlB4WlNNeDZyR0FDdVNNRlM3TEVDY1FaUXYwOEp3cG9wUmtxVmEwc2pReWRLZThnenJEaWlsYWUzaHcvcExoUlh3MWJLTDJwaXNoRjdOQ3JDUisycVR1WnlKM252eWNLR0xQKzBLcnBWWk9ZdHh2Wlc5OU41MzYyTUFOK3dDTWNGSThWYXphR29XRStiR1NZdldvV205VndFa0poYTZuMm5HSndLdWp0SE1RVmpyZEFYN2RzVjAvb1JRcjdIeDFZWG5QcVA3NjdZQlpRU29YME1ISWRBSFBKTmpEN2FWbDhrNHN6UThBUnA1NVZZT1c4WjVzZ1FQTlRTYjVhWGF2K2VMMHpBU294ZXZWdFh0LzY5eFpoL1IrV2xlQjZ3VGxjOGJkR0lLQ3BOUk5zUWNWMXdYanBXVGNUUzBDV21FbEZIRjZVU1lLUityYTBNc3JycTJib1UwR0FBQT0ifQ== -->

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":[""],"name":["_rn_"],"type":[""],"align":["left"]},{"label":["status"],"name":[1],"type":["chr"],"align":["left"]},{"label":["substatus"],"name":[2],"type":["chr"],"align":["left"]},{"label":["file"],"name":[3],"type":["chr"],"align":["left"]}],"data":[{"1":"unstaged","2":"modified","3":"../.Rbuildignore","_rn_":"1"},{"1":"unstaged","2":"modified","3":"../DESCRIPTION","_rn_":"2"},{"1":"unstaged","2":"modified","3":"../GAEZ_project_creation.Rmd","_rn_":"3"},{"1":"unstaged","2":"modified","3":"../GAEZ_project_creation.nb.html","_rn_":"4"},{"1":"untracked","2":"untracked","3":"../CONDUCT.md","_rn_":"5"},{"1":"untracked","2":"untracked","3":"../CONTRIBUTING.md","_rn_":"6"},{"1":"untracked","2":"untracked","3":"../Dockerfile","_rn_":"7"},{"1":"untracked","2":"untracked","3":".Rprofile","_rn_":"8"},{"1":"untracked","2":"untracked","3":".gitattributes","_rn_":"9"},{"1":"untracked","2":"untracked","3":".gitignore","_rn_":"10"},{"1":"untracked","2":"untracked","3":"GAEZ_site.Rproj","_rn_":"11"},{"1":"untracked","2":"untracked","3":"README.md","_rn_":"12"},{"1":"untracked","2":"untracked","3":"_workflowr.yml","_rn_":"13"},{"1":"untracked","2":"untracked","3":"code","_rn_":"14"},{"1":"untracked","2":"untracked","3":"data","_rn_":"15"},{"1":"untracked","2":"untracked","3":"output","_rn_":"16"},{"1":"untracked","2":"untracked","3":"site","_rn_":"17"},{"1":"untracked","2":"untracked","3":"../README.Rmd","_rn_":"18"},{"1":"untracked","2":"untracked","3":"../README.md","_rn_":"19"},{"1":"untracked","2":"untracked","3":"../analysis","_rn_":"20"},{"1":"untracked","2":"untracked","3":"../runtime.txt","_rn_":"21"}],"options":{"columns":{"min":{},"max":[10],"total":[3]},"rows":{"min":[10],"max":[10],"total":[21]},"pages":{}}}
  </script>
</div>

<!-- rnb-frame-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->


# Perform these steps for workflowr sub-folder
  1. rename 'analysis' to 'site'
  2. rename "site/about.Rmd" to "site/code.Rmd"
  2. create new Rmarkdown file "site/data.Rmd"

# Run workflowr code as chunk

<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxuc2V0d2QocGF0aClcbndmbG93X3B1Ymxpc2goYyhcXHNpdGUvaW5kZXguUm1kXFwsIFxcc2l0ZS9jb2RlLlJtZFxcLCBcXHNpdGUvZGF0YS5SbWRcXCwgXFxzaXRlL2xpY2Vuc2UuUm1kXFwpLCBcXFB1Ymxpc2ggdGhlIGluaXRpYWwgZmlsZXMgZm9yIG15cHJvamVjdFxcKVxuYGBgXG5gYGAifQ== -->

```r
```r
setwd(path)
wflow_publish(c(\site/index.Rmd\, \site/code.Rmd\, \site/data.Rmd\, \site/license.Rmd\), \Publish the initial files for myproject\)
```
```

<!-- rnb-source-end -->

<!-- rnb-output-begin eyJkYXRhIjoiRXJyb3IgaW4gcHJvY2Vzc19pbnB1dF9maWxlcyhmaWxlcywgYWxsb3dfbnVsbCA9IFRSVUUsIGZpbGVzX29ubHkgPSBGQUxTRSwgIDogXG4gIE5vdCBhbGwgZmlsZXMgZXhpc3QuIENoZWNrIHRoZSBwYXRocyB0byB0aGUgZmlsZXNcbiJ9 -->

```
Error in process_input_files(files, allow_null = TRUE, files_only = FALSE,  : 
  Not all files exist. Check the paths to the files
```



<!-- rnb-output-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->


#Integreate rrtools folder and workflowr folder:
Changes to rrtools folder (project folder):
  1. erase rrtools .gitignore and .profile
  2. rename analysis folder to 'results'
  3. move results/data files to data/
  4. erase R/ folder
  5. Create 'proj_setup' folder and save Project_creation.Rmd script in this folder
  6. move README.md in /output folder to data/derived/ and erase /output

Changes to workflowr folder (sub project folder):
  1. erase workflowr README.Rmd
  2. move README.Rmd in data folder to rrtools data folder and erase data folder
  3. erase workflowr Rproj file
  4. move all files from workflowr folder to main project folder, then erase workflowr folder
  5. add 'proj_setup/' to .gitignore

Commit changes with Git and push to GitHub.
In Github, set github project site to /docs in settings




<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuYGBgclxuI0NoZWNrIGlmIGFueSBkb2NzIGhhdmUgbm90IHlldCBiZWVuIHB1Ymxpc2hlZFxud2Zsb3dfc3RhdHVzKCkgXG4jIHNpbmdsZSBmaWxlXG53Zmxvd19wdWJsaXNoKFxcc2l0ZS9maWxlLlJtZFxcLCBcXEluZm9ybWF0aXZlIGNvbW1pdCBtZXNzYWdlXFwpXG4jIEFsbCB0cmFja2VkIGZpbGVzIHRoYXQgaGF2ZSBiZWVuIGVkaXRlZFxud2Zsb3dfcHVibGlzaChhbGwgPSBUUlVFLCBtZXNzYWdlID0gXFxJbmZvcm1hdGl2ZSBjb21taXQgbWVzc2FnZVxcKVxuIyBBIG5ldyBmaWxlIHBsdXMgYWxsIHRyYWNrZWQgZmlsZXMgdGhhdCBoYXZlIGJlZW4gZWRpdGVkXG53Zmxvd19wdWJsaXNoKFxcc2l0ZS9maWxlLlJtZFxcLCBcXEluZm9ybWF0aXZlIGNvbW1pdCBtZXNzYWdlXFwsIGFsbCA9IFRSVUUpXG4jIE11bHRpcGxlIGZpbGVzXG53Zmxvd19wdWJsaXNoKGMoXFxzaXRlL2ZpbGUuUm1kXFwsIFxcc2l0ZS9hbm90aGVyLlJtZFxcKSxcbiAgICAgICAgICAgICAgXFxJbmZvcm1hdGl2ZSBjb21taXQgbWVzc2FnZVxcKVxuIyBBbGwgUiBNYXJrZG93biBmaWxlcyB0aGF0IHN0YXJ0IHdpdGggdGhlIHBhdHRlcm4gXFxuZXdfXFxcbndmbG93X3B1Ymxpc2goXFxzaXRlL25ld18qUm1kXFwsIFxcSW5mb3JtYXRpdmUgY29tbWl0IG1lc3NhZ2VcXClcbiMgUmVwdWJsaXNoIGFsbCBwdWJsaXNoZWQgZmlsZXMgZXZlbiB0aG91Z2ggdGhleSBoYXZlbid0IGJlZW4gbW9kaWZpZWQuXG4jIFVzZWZ1bCBmb3IgY2hhbmdpbmcgc29tZSB1bml2ZXJzYWwgYXNwZWN0IG9mIHRoZSBzaXRlLCBlLmcuIHRoZSB0aGVtZVxuIyBzcGVjaWZpZWQgaW4gX3NpdGUueW1sLlxud2Zsb3dfcHVibGlzaChcXHNpdGUvX3NpdGUueW1sXFwsIFxcc2l0ZSB1cGRhdGVcXCwgcmVwdWJsaXNoID0gVFJVRSlcbiMgUHVibGlzaCBhbGwgcHJldmlvdXNseSBwdWJsaXNoZWQgZmlsZXMgdGhhdCBoYXZlIGJlZW4gY29tbWl0dGVkIG1vcmVcbiMgcmVjZW50bHkgdGhhbiB0aGVpciBjb3JyZXNwb25kaW5nIEhUTUwgZmlsZXMuIFRoaXMgaXMgdXNlZnVsIGlmIHlvdSBsaWtlIHRvXG4jIG1hbnVhbGx5IGNvbW1pdCB5b3VyIFIgTWFya2Rvd24gZmlsZXMuXG53Zmxvd19wdWJsaXNoKHVwZGF0ZSA9IFRSVUUpXG5cbndmbG93X3B1Ymxpc2goXFxzaXRlL2luZGV4LlJtZFxcLCBhbGwgPSBUUlVFLCBtZXNzYWdlID0gXFxVcGRhdGUgaW5kZXhcXClcbndmbG93X3B1Ymxpc2goXFxzaXRlL0VTR19Db3ZhcmlhdGVfUHJvY2Vzc2luZy5SbWRcXCwgYWxsID0gVFJVRSwgbWVzc2FnZSA9IFxcVXBkYXRlIEVTRyBjb3ZhcmlhdGUgcHJvY2Vzc2luZ1xcKVxuYGBgXG5gYGAifQ== -->

```r
```r
#Check if any docs have not yet been published
wflow_status() 
# single file
wflow_publish(\site/file.Rmd\, \Informative commit message\)
# All tracked files that have been edited
wflow_publish(all = TRUE, message = \Informative commit message\)
# A new file plus all tracked files that have been edited
wflow_publish(\site/file.Rmd\, \Informative commit message\, all = TRUE)
# Multiple files
wflow_publish(c(\site/file.Rmd\, \site/another.Rmd\),
              \Informative commit message\)
# All R Markdown files that start with the pattern \new_\
wflow_publish(\site/new_*Rmd\, \Informative commit message\)
# Republish all published files even though they haven't been modified.
# Useful for changing some universal aspect of the site, e.g. the theme
# specified in _site.yml.
wflow_publish(\site/_site.yml\, \site update\, republish = TRUE)
# Publish all previously published files that have been committed more
# recently than their corresponding HTML files. This is useful if you like to
# manually commit your R Markdown files.
wflow_publish(update = TRUE)

wflow_publish(\site/index.Rmd\, all = TRUE, message = \Update index\)
wflow_publish(\site/ESG_Covariate_Processing.Rmd\, all = TRUE, message = \Update ESG covariate processing\)
```
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->


<!-- rnb-text-begin -->



##Examples for making changes to project website with workflowr

<!-- rnb-text-end -->


<!-- rnb-chunk-begin -->


<!-- rnb-source-begin eyJkYXRhIjoiYGBgclxuI0NoZWNrIGlmIGFueSBkb2NzIGhhdmUgbm90IHlldCBiZWVuIHB1Ymxpc2hlZFxud2Zsb3dfc3RhdHVzKCkgXG4jIHNpbmdsZSBmaWxlXG53Zmxvd19wdWJsaXNoKFwic2l0ZS9maWxlLlJtZFwiLCBcIkluZm9ybWF0aXZlIGNvbW1pdCBtZXNzYWdlXCIpXG4jIEFsbCB0cmFja2VkIGZpbGVzIHRoYXQgaGF2ZSBiZWVuIGVkaXRlZFxud2Zsb3dfcHVibGlzaChhbGwgPSBUUlVFLCBtZXNzYWdlID0gXCJJbmZvcm1hdGl2ZSBjb21taXQgbWVzc2FnZVwiKVxuIyBBIG5ldyBmaWxlIHBsdXMgYWxsIHRyYWNrZWQgZmlsZXMgdGhhdCBoYXZlIGJlZW4gZWRpdGVkXG53Zmxvd19wdWJsaXNoKFwic2l0ZS9maWxlLlJtZFwiLCBcIkluZm9ybWF0aXZlIGNvbW1pdCBtZXNzYWdlXCIsIGFsbCA9IFRSVUUpXG4jIE11bHRpcGxlIGZpbGVzXG53Zmxvd19wdWJsaXNoKGMoXCJzaXRlL2ZpbGUuUm1kXCIsIFwic2l0ZS9hbm90aGVyLlJtZFwiKSxcbiAgICAgICAgICAgICAgXCJJbmZvcm1hdGl2ZSBjb21taXQgbWVzc2FnZVwiKVxuIyBBbGwgUiBNYXJrZG93biBmaWxlcyB0aGF0IHN0YXJ0IHdpdGggdGhlIHBhdHRlcm4gXCJuZXdfXCJcbndmbG93X3B1Ymxpc2goXCJzaXRlL25ld18qUm1kXCIsIFwiSW5mb3JtYXRpdmUgY29tbWl0IG1lc3NhZ2VcIilcbiMgUmVwdWJsaXNoIGFsbCBwdWJsaXNoZWQgZmlsZXMgZXZlbiB0aG91Z2ggdGhleSBoYXZlbid0IGJlZW4gbW9kaWZpZWQuXG4jIFVzZWZ1bCBmb3IgY2hhbmdpbmcgc29tZSB1bml2ZXJzYWwgYXNwZWN0IG9mIHRoZSBzaXRlLCBlLmcuIHRoZSB0aGVtZVxuIyBzcGVjaWZpZWQgaW4gX3NpdGUueW1sLlxud2Zsb3dfcHVibGlzaChcInNpdGUvX3NpdGUueW1sXCIsIFwic2l0ZSB1cGRhdGVcIiwgcmVwdWJsaXNoID0gVFJVRSlcbiMgUHVibGlzaCBhbGwgcHJldmlvdXNseSBwdWJsaXNoZWQgZmlsZXMgdGhhdCBoYXZlIGJlZW4gY29tbWl0dGVkIG1vcmVcbiMgcmVjZW50bHkgdGhhbiB0aGVpciBjb3JyZXNwb25kaW5nIEhUTUwgZmlsZXMuIFRoaXMgaXMgdXNlZnVsIGlmIHlvdSBsaWtlIHRvXG4jIG1hbnVhbGx5IGNvbW1pdCB5b3VyIFIgTWFya2Rvd24gZmlsZXMuXG53Zmxvd19wdWJsaXNoKHVwZGF0ZSA9IFRSVUUpXG5cbndmbG93X3B1Ymxpc2goXCJzaXRlL2luZGV4LlJtZFwiLCBhbGwgPSBUUlVFLCBtZXNzYWdlID0gXCJVcGRhdGUgaW5kZXhcIilcbndmbG93X3B1Ymxpc2goXCJzaXRlL0VTR19Db3ZhcmlhdGVfUHJvY2Vzc2luZy5SbWRcIiwgYWxsID0gVFJVRSwgbWVzc2FnZSA9IFwiVXBkYXRlIEVTRyBjb3ZhcmlhdGUgcHJvY2Vzc2luZ1wiKVxuYGBgIn0= -->

```r
#Check if any docs have not yet been published
wflow_status() 
# single file
wflow_publish("site/file.Rmd", "Informative commit message")
# All tracked files that have been edited
wflow_publish(all = TRUE, message = "Informative commit message")
# A new file plus all tracked files that have been edited
wflow_publish("site/file.Rmd", "Informative commit message", all = TRUE)
# Multiple files
wflow_publish(c("site/file.Rmd", "site/another.Rmd"),
              "Informative commit message")
# All R Markdown files that start with the pattern "new_"
wflow_publish("site/new_*Rmd", "Informative commit message")
# Republish all published files even though they haven't been modified.
# Useful for changing some universal aspect of the site, e.g. the theme
# specified in _site.yml.
wflow_publish("site/_site.yml", "site update", republish = TRUE)
# Publish all previously published files that have been committed more
# recently than their corresponding HTML files. This is useful if you like to
# manually commit your R Markdown files.
wflow_publish(update = TRUE)

wflow_publish("site/index.Rmd", all = TRUE, message = "Update index")
wflow_publish("site/ESG_Covariate_Processing.Rmd", all = TRUE, message = "Update ESG covariate processing")
```

<!-- rnb-source-end -->

<!-- rnb-chunk-end -->

