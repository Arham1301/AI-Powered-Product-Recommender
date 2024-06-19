import json

# Example Python dictionary (replace this with your actual dictionary)
socks_dict = {
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfYXRmOjIwMDExNDU0MDQxNzA5ODo6MDo6&url=%2FAmazon-Essentials-Performance-Cushioned-Athletic%2Fdp%2FB09YF5MPWQ%2Fref%3Dsr_1_1_ffob_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1": {
        "% Cotton": 61.0,
        "% Polyester": 32.0,
        "% Nylon": 4.0,
        "% Elastane": 3.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfYXRmOjMwMDE3MjcwMjk3NjUwMjo6MDo6&url=%2FFITRELL-Athletic-Cushioned-Sports-Running%2Fdp%2FB08C77J24W%2Fref%3Dsr_1_2_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-2-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1": {
        "% Cotton": 76.2,
        "% Polyester": 14.0,
        "% Nylon": 6.5,
        "% Spandex": 3.3
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfYXRmOjMwMDEyNjQzODQ1NzIwMjo6MDo6&url=%2FHOT-FEET-Moisture-Cushioned-Reinforced%2Fdp%2FB082BFKMBQ%2Fref%3Dsr_1_3_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-3-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1": {
        "% Cotton": 70.0,
        "% Polyester": 27.0,
        "% Spandex": 2.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfYXRmOjIwMDAxOTE3MTc0MDkzMTo6MDo6&url=%2FCompression-Running-Cycling-Fasciitis-Athletic%2Fdp%2FB07W5T9M37%2Fref%3Dsr_1_4_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-4-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1": {},
    "https://www.amazon.com//Hanes-Moisture-wicking-Available-14-packs-Athletic-socks/dp/B002HL5GKE/ref=sr_1_5?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-5": {
        "% Cotton": 76.0,
        "% Polyester": 22.0,
        "% Spandex": 1.0,
        "% Other": 1.0
    },
    "https://www.amazon.com//Dickies-Multi-Pack-Dri-Tech-Moisture-Control/dp/B004QF0TFQ/ref=sr_1_6?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-6": {
        "% Cotton": 78.0,
        "% Polyester": 19.0,
        "% Spandex": 2.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//adidas-Mens-Athletic-Black-Aluminum/dp/B008YA0Z44/ref=sr_1_7?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-7": {
        "% Polyester": 97.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Fruit-Loom-Defense-Socks-black/dp/B07VNHNWPL/ref=sr_1_8?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-8": {
        "% Polyester": 97.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Hanes-12-Pack-FreshIQ-Socks-White/dp/B00MDZWPEO/ref=sr_1_9?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-9": {
        "% Polyester": 56.0,
        "% Cotton": 43.0,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//Hanes-Womens-Cushioned-Athletic-10/dp/B00JVTNWB0/ref=sr_1_10?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-10": {
        "% Polyester": 59.0,
        "% Cotton": 39.0,
        "% Spandex": 1.0,
        "% Other": 1.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjIwMDAxMTk1NDQ0ODYzMTo6MDo6&url=%2FAmazon-Essentials-Performance-Cushioned-Athletic%2Fdp%2FB07F282SF7%2Fref%3Dsr_1_11_ffob_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-11-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {
        "% Cotton": 62.0,
        "% Polyester": 30.0,
        "% Nylon": 6.0,
        "% Elastane": 2.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjMwMDExODUwMzAyOTAwMjo6MDo6&url=%2FCHARMKING-Cotton-Classic-Casual-Multicolor%2Fdp%2FB0BW5LZ2LS%2Fref%3Dsr_1_12_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-12-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {
        "% Cotton": 88.0,
        "% Polyester": 10.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjMwMDAxNzY4MTAzNzAwMjo6MDo6&url=%2FDoctors-Select-Bamboo-Diabetic-Socks%2Fdp%2FB0BNPSTKJ1%2Fref%3Dsr_1_13_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-13-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {
        "% Viscose": 49.0,
        "% Polyester": 49.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjIwMDAyOTIwNDg0OTU5ODo6MDo6&url=%2FCooplus-Athletic-Cushioned-Breathable-Support%2Fdp%2FB07LFYM6BZ%2Fref%3Dsr_1_14_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-14-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {
        "% Polyester": 93.0,
        "% Spandex": 4.0,
        "% Nylon": 3.0
    },
    "https://www.amazon.com//Womens-Mini-Crew-6-Pack-White/dp/B00A9MQD8C/ref=sr_1_15?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-15": {
        "% Cotton": 79.0,
        "% Nylon": 15.0,
        "% Polyester": 5.0,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//Hanes-Ultimate-Womens-6-Pack-Ankle/dp/B014D3KZIQ/ref=sr_1_16?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-16": {
        "% Polyester": 98.0,
        "% Spandex": 1.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//Hanes-Womens-Crew-White-10/dp/B00HVWSQG0/ref=sr_1_17?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-17": {
        "% Cotton": 76.0,
        "% Polyester": 22.0,
        "% Spandex": 1.0,
        "% Other": 1.0
    },
    "https://www.amazon.com//Fruit-Loom-Cushion-Defense-Ankle/dp/B07VF6N878/ref=sr_1_18?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-18": {
        "% Polyester": 97.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjMwMDA2NDA4MzE1OTkwMjo6MDo6&url=%2FCopper-Compression-Socks-Women-Circulation%2Fdp%2FB0C5MH2YSY%2Fref%3Dsr_1_19_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-19-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {
        "% Nylon": 85.0,
        "% Polyester": 15.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjMwMDAyNTU5MTU4MDkwMjo6MDo6&url=%2FBUDERMMY-Compression-Support-Athletic-Running%2Fdp%2FB0C459JZT2%2Fref%3Dsr_1_20_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-20-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {
        "% Nylon": 65.0,
        "% cotton": 25.0,
        "% Spandex": 10.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjMwMDE0NjQ4NTMzNjUwMjo6MDo6&url=%2FJ-BOX-Athletic-Quarter-Breathable-Running%2Fdp%2FB0CNW1BRLM%2Fref%3Dsr_1_21_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-21-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {
        "% cotton": 95.1,
        "% polyester": 2.1,
        "% spandex": 2.8
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo0ODEwODk4Njg2MTIwMTQwOjE3MTg2NjE1NjA6c3BfbXRmOjMwMDIyNDgzMjI1NzUwMjo6MDo6&url=%2FSocks-Women-Womens-Clothing-X16-Hun24-M%2Fdp%2FB0CM9KZB5X%2Fref%3Dsr_1_22_sspa%3Fdib%3DeyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c%26dib_tag%3Dse%26keywords%3Dsocks%26qid%3D1718661560%26sr%3D8-22-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1": {},
    "https://www.amazon.com//Champion-Double-Moisture-Wicking-6-Pack/dp/B07SGYBB7D/ref=sr_1_23?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-23": {
        "% Polyester": 100.0
    },
    "https://www.amazon.com//ACCFOD-Womens-White-Athletic-Running/dp/B0C471XYPX/ref=sr_1_24?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-24": {},
    "https://www.amazon.com//Dickies-Multi-Pack-Dri-tech-Moisture-Control/dp/B00AECT1ZE/ref=sr_1_25?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-25": {
        "% Cotton": 70.0,
        "% Polyester": 28.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//adidas-Mens-6-Pack-White-Black/dp/B000M25HZ4/ref=sr_1_26?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-26": {
        "% Polyester": 97.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Unisex-Performance-Cushion-Socks-Medium/dp/B010RWD22S/ref=sr_1_27?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-27": {
        "% Cotton": 76.0,
        "% Nylon": 21.0,
        "% Spandex": 2.0,
        "% Polyester": 1.0
    },
    "https://www.amazon.com//Hanes-Mens-Cushion-Socks-6-Pair/dp/B08MBFGL13/ref=sr_1_28?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-28": {
        "% Polyester": 50.0,
        "% Cotton": 39.0,
        "% Rayon": 8.0,
        "% Spandex": 2.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//CelerSport-Ankle-Athletic-Running-Medium/dp/B07G996FY9/ref=sr_1_29?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-29": {
        "% Combed": 88.3,
        "% Polyester": 10.7,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo1ODM1OTY5NzI3OTkyOTg3OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljOjMwMDE3MjcwMjk3NjUwMjo6MDo6&url=%2FFITRELL-Athletic-Cushioned-Sports-Running%2Fdp%2FB08C77J24W%2Fref%3Dsxin_37_pa_sp_search_thematic_sspa%3Fcontent-id%3Damzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%253Aamzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.XUeWGdChWguxDJ8MHT0yEeN_zCeWzyxHQfG2ZW8RoYJgW3tDpZx4ZFHhEnd_TnbZ.HSeESYWayJ6JePBfItvawWwPMX71Fo7gd1L9OmV28Nw%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB08C77J24W%26pd_rd_r%3Dcd2283a4-b7c9-49be-8142-e3a2c8cf6524%26pd_rd_w%3DHP5Ca%26pd_rd_wg%3Dif1v5%26pf_rd_p%3D0f20b18b-b203-4567-90be-639d12f5f08d%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DTc8eqSFhUl4VwMzbE4fw%252Fw%253D%253D%26sr%3D1-1-183302c6-8dec-4386-8e58-6031e7be5ad8-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM%26psc%3D1": {
        "% Cotton": 76.2,
        "% Polyester": 14.0,
        "% Nylon": 6.5,
        "% Spandex": 3.3
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo1ODM1OTY5NzI3OTkyOTg3OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljOjMwMDEyNjQzODQ1NzIwMjo6MTo6&url=%2FHOT-FEET-Moisture-Cushioned-Reinforced%2Fdp%2FB082BFKMBQ%2Fref%3Dsxin_37_pa_sp_search_thematic_sspa%3Fcontent-id%3Damzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%253Aamzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.XUeWGdChWguxDJ8MHT0yEeN_zCeWzyxHQfG2ZW8RoYJgW3tDpZx4ZFHhEnd_TnbZ.HSeESYWayJ6JePBfItvawWwPMX71Fo7gd1L9OmV28Nw%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB082BFKMBQ%26pd_rd_r%3Dcd2283a4-b7c9-49be-8142-e3a2c8cf6524%26pd_rd_w%3DHP5Ca%26pd_rd_wg%3Dif1v5%26pf_rd_p%3D0f20b18b-b203-4567-90be-639d12f5f08d%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sr%3D1-2-183302c6-8dec-4386-8e58-6031e7be5ad8-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM%26psc%3D1": {
        "% Cotton": 70.0,
        "% Polyester": 27.0,
        "% Spandex": 2.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo1ODM1OTY5NzI3OTkyOTg3OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljOjIwMDAyOTIwNDg0OTU5ODo6Mzo6&url=%2FCooplus-Athletic-Cushioned-Breathable-Support%2Fdp%2FB07LFYM6BZ%2Fref%3Dsxin_37_pa_sp_search_thematic_sspa%3Fcontent-id%3Damzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%253Aamzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.XUeWGdChWguxDJ8MHT0yEeN_zCeWzyxHQfG2ZW8RoYJgW3tDpZx4ZFHhEnd_TnbZ.HSeESYWayJ6JePBfItvawWwPMX71Fo7gd1L9OmV28Nw%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB07LFYM6BZ%26pd_rd_r%3Dcd2283a4-b7c9-49be-8142-e3a2c8cf6524%26pd_rd_w%3DHP5Ca%26pd_rd_wg%3Dif1v5%26pf_rd_p%3D0f20b18b-b203-4567-90be-639d12f5f08d%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sr%3D1-3-183302c6-8dec-4386-8e58-6031e7be5ad8-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM%26psc%3D1": {
        "% Polyester": 93.0,
        "% Spandex": 4.0,
        "% Nylon": 3.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTo1ODM1OTY5NzI3OTkyOTg3OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljOjMwMDA5NTQzMjIwNTAwMjo6NDo6&url=%2FRunning-Hylaea-Moisture-Wicking-Athletic%2Fdp%2FB089B11ZSW%2Fref%3Dsxin_37_pa_sp_search_thematic_sspa%3Fcontent-id%3Damzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%253Aamzn1.sym.0f20b18b-b203-4567-90be-639d12f5f08d%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.XUeWGdChWguxDJ8MHT0yEeN_zCeWzyxHQfG2ZW8RoYJgW3tDpZx4ZFHhEnd_TnbZ.HSeESYWayJ6JePBfItvawWwPMX71Fo7gd1L9OmV28Nw%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB089B11ZSW%26pd_rd_r%3Dcd2283a4-b7c9-49be-8142-e3a2c8cf6524%26pd_rd_w%3DHP5Ca%26pd_rd_wg%3Dif1v5%26pf_rd_p%3D0f20b18b-b203-4567-90be-639d12f5f08d%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sr%3D1-4-183302c6-8dec-4386-8e58-6031e7be5ad8-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM%26psc%3D1": {},
    "https://www.amazon.com//adidas-Cushioned-Athletic-Quarter-Aluminum/dp/B008YA0ZO4/ref=sr_1_30?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-30": {
        "% Polyester": 97.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Saucony-Womens-Performance-Athletic-Assorted/dp/B07LGVXPXK/ref=sr_1_31?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-31": {
        "% Polyester": 98.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//Saucony-Ventilating-Performance-Comfort-No-Show/dp/B01D2GRTIE/ref=sr_1_32?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-32": {
        "% Polyester": 98.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//COOVAN-Cushion-Comfort-Breathable-Casual/dp/B07MGZYK6R/ref=sr_1_33?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-33": {},
    "https://www.amazon.com//Show-Socks-Cotton-Invisible-10-12/dp/B07VCHHXN3/ref=sr_1_34?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-34": {
        "% Cotton": 85.0,
        "% Polyester": 12.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Hanes-Womens-Lightweight-Breathable-Accent/dp/B084R3MZ6J/ref=sr_1_35?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-35": {
        "% Polyester": 97.0,
        "% Spandex": 2.0,
        "% Other": 1.0
    },
    "https://www.amazon.com//Smiling-Elastic-Aesthetic-Lightweight-Collocation/dp/B0B2RMCCJS/ref=sr_1_36?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-36": {},
    "https://www.amazon.com//Amazon-Essentials-Performance-Cushioned-Athletic/dp/B07F282SF7/ref=sr_1_37?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-37": {
        "% Cotton": 62.0,
        "% Polyester": 30.0,
        "% Nylon": 6.0,
        "% Elastane": 2.0
    },
    "https://www.amazon.com//COOVAN-Pairs-Comfort-Cushion-Casual/dp/B09NM221JM/ref=sr_1_38?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-38": {},
    "https://www.amazon.com//IDEGG-Cotton-Casual-Anti-Slid-Athletic/dp/B07D1ZWVB6/ref=sr_1_39?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-39": {
        "% Cotton": 80.0,
        "% Polyester": 17.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Hanes-Double-12-pair-Available-fashion/dp/B00IO9H6QU/ref=sr_1_40?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-40": {
        "% Polyester": 59.0,
        "% Cotton": 40.0,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//Women-Socks-Invisible-Loafer-Liners/dp/B07WT225KN/ref=sr_1_41?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-41": {},
    "https://www.amazon.com//Unisex-Performance-Cushion-Training-Medium/dp/B01ABVLOHA/ref=sr_1_42?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-42": {},
    "https://www.amazon.com//Double-6-Pair-Pack-Cotton-Rich-Socks/dp/B003YJBYPE/ref=sr_1_43?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-43": {
        "% Textile": 100.0
    },
    "https://www.amazon.com//PUMA-mens-Running-Socks-Black/dp/B07NNTCV5K/ref=sr_1_44?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-44": {
        "% Polyester": 98.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//Fruit-Loom-Defense-Socks-White/dp/B07NGT67H8/ref=sr_1_45?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-45": {
        "% Polyester": 97.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Gildan-Performance-Socks-12-Pairs-White/dp/B08WWT83PH/ref=sr_1_46?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-46": {
        "% Polyester": 97.0,
        "% Spandex": 3.0
    },
    "https://www.amazon.com//Armour-Training-Cotton-Quarter-6-Pair/dp/B07V7SFCXL/ref=sr_1_47?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-47": {
        "% Cotton": 76.0,
        "% Nylon": 22.0,
        "% Polyester": 1.0,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//Hanes-Moisture-Wicking-Available-14-Packs-White-14/dp/B0BXT3WL1F/ref=sr_1_48?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-48": {
        "% Cotton": 73.0,
        "% Polyester": 25.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//PUMA-womens-Running-Socks-11-Sep/dp/B07PWNK5T6/ref=sr_1_49?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-49": {
        "% Polyester": 98.0,
        "% Spandex": 2.0
    },
    "https://www.amazon.com//Gold-Toe-656S-Athletic-Multi-Pack/dp/B0002TP1D0/ref=sr_1_50?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-50": {
        "% Cotton": 81.0,
        "% Nylon": 18.0,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//Hanes-Cushion-Socks-6-Pair-Available/dp/B08MBC71ML/ref=sr_1_51?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-51": {
        "% Cotton": 44.0,
        "% Nylon": 1.0,
        "% Polyester": 45.0,
        "% Spandex": 1.0,
        "% Rayon": 9.0
    },
    "https://www.amazon.com//Fruit-Loom-Everyday-Socks-Black/dp/B0735T525V/ref=sr_1_52?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-52": {
        "% Cotton": 55.0,
        "% Polyester": 45.0
    },
    "https://www.amazon.com//Under-Armour-Resistor-Graphite-X-Large/dp/B013CSL18Q/ref=sr_1_53?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-53": {
        "% Polyester": 97.0,
        "% Spandex": 2.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//Dickies-Dri-tech-Moisture-Multipack-Essential/dp/B08TPDKWH2/ref=sr_1_54?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-54": {
        "% Polyester": 73.0,
        "% Cotton": 25.0,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//Gildan-Mens-Cotton-Socks-White/dp/B086DXQD6T/ref=sr_1_55?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-55": {
        "% Cotton": 72.0,
        "% Polyester": 24.0,
        "% Spandex": 3.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//Ankle-Socks-Cotton-Casual-Non-Slip/dp/B071114HR9/ref=sr_1_56?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-56": {
        "%Cotton": 80.0,
        "%Polyester": 17.0,
        "%Spandex": 3.0
    },
    "https://www.amazon.com//Gold-Toe-656P-Quarter-Athletic/dp/B000SP6UVK/ref=sr_1_57?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-57": {
        "% Cotton": 81.0,
        "% Polyester": 16.0,
        "% Nylon": 18.0,
        "% Spandex": 1.0
    },
    "https://www.amazon.com//Cooplus-Athletic-Cushioned-Breathable-Support/dp/B07LFYM6BZ/ref=sr_1_58?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-58": {
        "% Polyester": 93.0,
        "% Spandex": 4.0,
        "% Nylon": 3.0
    },
    "https://www.amazon.com//Terry-Cut-Cool-White-Traditional-10-13/dp/B06XKXTDLS/ref=sr_1_59?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-59": {
        "% Polyester": 65.0,
        "% Cotton": 30.0,
        "% Spandex": 5.0
    },
    "https://www.amazon.com//HUE-Womens-Slouch-Sock-White/dp/B08QB466RB/ref=sr_1_60?dib=eyJ2IjoiMSJ9.WRlEHpAoRPrmxDpK2nsOqEWyUo7G328fv8xd-QhtYC1ec2TTMzEocOwnr-x3sta11NnX_iwmUS6-k5fxMfKQqoceHWxGPuIkQBJHlX4FRt1ix0P1MrchqeJabklupJFRupuMUL3_AOF4bO6R0CH_lI6bvEGy9ZvzZRVZdt_Je5KVAZy_KJn8jBPfSbUqddQc6DvNaPX7TLfolIJNnVeVcdMSSIaVqVNwLYYsLbsPRMmGqeUGxElNKCB6-1LTPI7CmhSeRxG_Npt0cqORErnBv_5tLQee_gnib9zGEIir--c.gXV2ZYS5CMRPoDY9NAIK0OQFl_WCJnWF3BHSHREIq3c&dib_tag=se&keywords=socks&qid=1718661560&sr=8-60": {
        "% Cotton": 90.0,
        "% Nylon": 8.0,
        "% Spandex": 1.0,
        "% Polypropylene": 1.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTozNjE2MDA4ODg0ODA1NDE5OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljX2J0ZjozMDAwNjg2NDU4OTIxMDI6OjE6Og&url=%2FHOT-FEET-Moisture-Cushioned-Reinforced%2Fdp%2FB082BF9MPC%2Fref%3Dsxbs_pa_sp_search_thematic_btf_sspa%3Fcontent-id%3Damzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%253Aamzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.JJa369-stRsskQCAQLSPgfIVzeLkNqadMqwDwGJLMxaUuVB6Mq10cLAF1db8bkPt.gF9Fw7a0sjEFOaEHf50Oeb8fa9dLiFrkQOmfOooHbHQ%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB082BF9MPC%26pd_rd_r%3D0ee13a1a-d8dd-407e-b0be-a885589b1feb%26pd_rd_w%3DhdQut%26pd_rd_wg%3DsK2N6%26pf_rd_p%3Db73ec481-6b55-412e-9a8f-1b955990a59c%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sr%3D1-1-0593f4a3-2672-42a2-bca6-c8b865efb498-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWNfYnRm%26psc%3D1": {
        "% Cotton": 70.0,
        "% Polyester": 27.0,
        "% Spandex": 2.0,
        "% Nylon": 1.0
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTozNjE2MDA4ODg0ODA1NDE5OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljX2J0ZjozMDAxNzIzMzU5NzE4MDI6OjI6Og&url=%2FCotton-Breathable-Athletic-Running-Multi-color%2Fdp%2FB0CDGQVMK1%2Fref%3Dsxbs_pa_sp_search_thematic_btf_sspa%3Fcontent-id%3Damzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%253Aamzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.JJa369-stRsskQCAQLSPgfIVzeLkNqadMqwDwGJLMxaUuVB6Mq10cLAF1db8bkPt.gF9Fw7a0sjEFOaEHf50Oeb8fa9dLiFrkQOmfOooHbHQ%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB0CDGQVMK1%26pd_rd_r%3D0ee13a1a-d8dd-407e-b0be-a885589b1feb%26pd_rd_w%3DhdQut%26pd_rd_wg%3DsK2N6%26pf_rd_p%3Db73ec481-6b55-412e-9a8f-1b955990a59c%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sr%3D1-2-0593f4a3-2672-42a2-bca6-c8b865efb498-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWNfYnRm%26psc%3D1": {
        "% cotton": 95.1,
        "% polyester": 2.1,
        "% spandex": 2.8
    },
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTozNjE2MDA4ODg0ODA1NDE5OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljX2J0ZjozMDAwNDI1MDY2MjQxMDI6OjM6Og&url=%2FCOOVAN-Cushion-Comfort-Breathable-Casual%2Fdp%2FB07MGZYK6R%2Fref%3Dsxbs_pa_sp_search_thematic_btf_sspa%3Fcontent-id%3Damzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%253Aamzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.JJa369-stRsskQCAQLSPgfIVzeLkNqadMqwDwGJLMxaUuVB6Mq10cLAF1db8bkPt.gF9Fw7a0sjEFOaEHf50Oeb8fa9dLiFrkQOmfOooHbHQ%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB07MGZYK6R%26pd_rd_r%3D0ee13a1a-d8dd-407e-b0be-a885589b1feb%26pd_rd_w%3DhdQut%26pd_rd_wg%3DsK2N6%26pf_rd_p%3Db73ec481-6b55-412e-9a8f-1b955990a59c%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sr%3D1-3-0593f4a3-2672-42a2-bca6-c8b865efb498-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWNfYnRm%26psc%3D1": {},
    "https://www.amazon.com//sspa/click?ie=UTF8&spc=MTozNjE2MDA4ODg0ODA1NDE5OjE3MTg2NjE1NjA6c3Bfc2VhcmNoX3RoZW1hdGljX2J0ZjoyMDAxNjgxOTgzMDIwOTg6OjQ6Og&url=%2FAiracker-Athletic-Performance-Cushioned-Breathable%2Fdp%2FB08LNB8XFQ%2Fref%3Dsxbs_pa_sp_search_thematic_btf_sspa%3Fcontent-id%3Damzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%253Aamzn1.sym.b73ec481-6b55-412e-9a8f-1b955990a59c%26cv_ct_cx%3Dsocks%26dib%3DeyJ2IjoiMSJ9.JJa369-stRsskQCAQLSPgfIVzeLkNqadMqwDwGJLMxaUuVB6Mq10cLAF1db8bkPt.gF9Fw7a0sjEFOaEHf50Oeb8fa9dLiFrkQOmfOooHbHQ%26dib_tag%3Dse%26keywords%3Dsocks%26pd_rd_i%3DB08LNB8XFQ%26pd_rd_r%3D0ee13a1a-d8dd-407e-b0be-a885589b1feb%26pd_rd_w%3DhdQut%26pd_rd_wg%3DsK2N6%26pf_rd_p%3Db73ec481-6b55-412e-9a8f-1b955990a59c%26pf_rd_r%3DZJJHYT7QFBNXNV3KMRMR%26qid%3D1718661560%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sr%3D1-4-0593f4a3-2672-42a2-bca6-c8b865efb498-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWNfYnRm%26psc%3D1": {
        "% Polyester": 86.5,
        "% Spandex": 13.5
    }
}

# Convert dictionary to JSON formatted string
json_data = json.dumps(socks_dict, indent=2)  # indent for pretty printing with 2 spaces

# Write JSON data to a file
with open('socks.json', 'w') as json_file:
    json_file.write(json_data)

print("JSON data has been written to socks.json file.")

