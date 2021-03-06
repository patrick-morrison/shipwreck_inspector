library(tidyverse)
library(rvest)
library(xml2)

wrecks <- tibble(url = read_xml('https://shipwreckswa.com/wp-sitemap-posts-post-1.xml') %>% 
  xml_children() %>% xml_text('loc'))

get_wrecked <- function(url) {
  html <- read_html(url)
  
  d <- data.frame(
    id = NA
  )
  
  d$name <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[1]/div/div/div[1]/div/div/div/div/h1') %>% 
    html_text()
  
  d$user <-  1
  
  d$sunk <-  ''
  d$built <-  ''
  
  d$built_details <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[11]/div/div/div[2]/div/div/div/div/div') %>% 
    html_text()
  
  d$description <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[5]/div/div/div[2]/div/div/div/div/div') %>% 
    html_text()
  
  d$construction <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[7]/div/div/div[2]/div/div/div/div/div') %>% 
    html_text()
  
  d$owner <- html %>% 
    html_element(xpath='//html/body/div[2]/div/div/section[5]/div/div/div[4]/div/div/div/div/div') %>% 
    html_text()
  
  d$size <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[9]/div/div/div[2]/div/div/div/div/div') %>% 
    html_text()
  
  d$sinking <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[7]/div/div/div[2]/div/div/div/div/div') %>% 
    html_text()
  
  d$location <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[11]/div/div/div[4]/div/div/div/div/div') %>% 
    html_text()
  
  d$underwater <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[9]/div/div/div[4]/div/div/div/div/div') %>% 
    html_text()
  
  d$sinking <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[13]/div/div/div[4]/div/div/div/div/div') %>% 
    html_text()
  
  d$region <- ''
  
  
  d$latitude <- html %>% 
    html_element(xpath='/html/body/div[2]/div/div/section[15]/div/div/div[5]/div/div/div/div/div') %>% 
    html_text()
  
  d$longitude <- html %>% 
    html_element(xpath='//html/body/div[2]/div/div/section[15]/div/div/div[2]/div/div/div/div/div') %>% 
    html_text()
  
  d$image <- ''
  d$caption <- ''
  
  d$museum_link <- ''
  d$dave_link <- ''
  
  return(d)
}

wrecks_with_data <- wrecks %>% 
  mutate(data = map(url, get_wrecked)) %>% 
  unnest_wider(col = data)

wrecks_with_data_clean <- wrecks_with_data %>% 
  rownames_to_column('row') %>% 
  mutate(id = parse_number(row) + 200,
         name = str_to_title(name)) %>% 
  select(-row)

write_csv(wrecks_with_data_clean, 'shipwrecks_wa.csv')

#Other cleaning

full <- read_csv("shipwrecks_wa_seed.csv") %>% select(-built_details)
overwrite <- read_csv("wip/shipwrecks_wa.csv") %>% select(id, built_details)
amended <- full %>% left_join(overwrite)

write_csv(amended, 'shipwrecks_wa_amended.csv')
#wrecks <- read_csv("shipwrecks_wa_seed.csv")
#wrecks[duplicated(wrecks$name),]
