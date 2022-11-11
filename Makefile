choice_offers.db : choice_offers.csv
	csvs-to-sqlite $^ $@
	sqlite-utils extract $@ choice_offers masked_ID level year --table applicant --fk-column applicant_id

choice_offers.csv : FOIA11525_2018.csv FOIA11525_2020.csv	\
                    FOIA11525_2022.csv FOIA11525_2019.csv	\
                    FOIA11525_2021.csv
	csvstack $^ | \
            python scripts/split_types.py > $@

%.csv : raw/%.xlsx
	in2csv $< > $@
