import sys
import re

def get_title_from_user(orig_title_="0001_Proj_ch1_(chapter_title"):
	req_title_ = input("Hello, what is the video to be renamed? \n...")
	res_ = re.split('_', req_title_)
	def_list_ = re.split('_', orig_title_)

	return res_ if len(res_) > 3 else def_list_

def get_full_title(list_, chron_, proj_, chap_num, chap_titl_):

	full_title =  chron_ + list_[0] + proj_ + list_[1] + chap_num + list_[2] + chap_titl_
	return full_title

def clean(word_):
	new_word = re.sub(r"[()]", "", word_)
	return new_word


print(get_title_from_user())

sys.exit(0)

new_joins = [": ", "—", ", "]

# if len(result) >= 3:
# 	 chron_number, project_title, chapter_number = [str_.title() for str_ in result[:3]]
# else:



c1 = result[3:]
c2 = [clean(word.title()) for word in c1]
chapter_title = " ".join(c2)

new_title = get_full_title(new_joins, chron_number, project_title, chapter_number, chapter_title)
print(new_title)

"""new_joins = dict(
	[
		('post_titl',':')
		,('post_proj','--')
		, ('post_chap',',')
	]
)"""
