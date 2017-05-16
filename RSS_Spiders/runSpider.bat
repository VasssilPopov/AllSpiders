scrapy runspider Dnevnik.py -o Reports/Dnevnik-%1.json -t jl>Outputs/DnevnikOutput.txt
scrapy runspider PIK.py -o Reports/PIK-%1.json -t jl>Outputs/PIKOutput.txt
scrapy runspider SegaBG.py -o Reports/SegaBG-%1.json -t jl>Outputs/SegaBGOutput.txt
scrapy runspider Mediapool.py -o Reports/Mediapool-%1.json -t jl>Outputs/MediapoolOutput.txt
scrapy runspider ClubZ.py -o Reports/ClubZ-%11.json -t jl>Outputs/ClubZOutput.txt
scrapy runspider Epicenter.py -o Reports/Epicenter-%1.json -t jl>Outputs/EpicenterOutput.txt
