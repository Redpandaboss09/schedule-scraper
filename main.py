import scraper
import pdf_creator
import data_cleaner

pdf_creator.create_schedule(data_cleaner.fix_data(scraper.caller()))

print('PDF CREATED! \n \n')
input('Press ENTER to exit...')