from sqlalchemy import Integer, and_, not_, cast, func, insert, inspect, or_, select, text, String
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload
import pandas as pd

from src.database import Base, sync_engine, session
from src.section_models import (
                        Section, SectionProperty, SectionSeries, SectionSizeGroup,
                        SectionSizes, SectionSpecies, SectionType, SectionValue, SectionVariable
                           )





class SyncORM:
    
    @staticmethod
    def properties_control():
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_colwidth', None)
    
        value1 = int(input("Write the PROPERTY ID: "))
        value2 = int(input("Write the section shape ID: "))
        value3 = input("Write the reference formula: ")
        
        with session() as sess:
            query = (
                select(
                    SectionProperty.ng_idsectionvariable.label('Variable_ID'),
                    SectionProperty.ng_formula0.label('Formula'),
                    SectionSeries.ng_sectionseries.label('Series_Name'),
                    SectionSeries.ng_sectionshape.label('Shape_ID'),
                    SectionSeries.id.label('Section_ID')
                )
                .join(SectionSeries, SectionSeries.id == SectionProperty.pid)
                .filter(and_(
                        SectionProperty.ng_idsectionvariable == value1,
                        SectionSeries.ng_sectionshape == value2,
                        not_(SectionProperty.ng_formula0.like(value3))
                ))

             )
            
            res = sess.execute(query)
            df = pd.DataFrame(res.fetchall(), columns=res.keys())
            df['section_link'] = "https://ng.dlubal.com/default.aspx?form=486&id=" + df['Section_ID'].astype(str) + "&viewpage=872"
            print(df)
            
    @staticmethod
    def values_control():
        
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_colwidth', None)
        
        section_id = int(input("Write the section ID: "))
        
        with session() as sess:
            query = (
                select(
                    SectionSeries.id.label('Series_ID'),
                    SectionSeries.ng_sectionseries.label('Series_Name'),
                    Section.id.label('Section_ID'),
                    Section.ng_section.label('Section_Name'),
                    SectionVariable.ng_sectionvariable.label('Var_name'),
                    SectionValue.ng_value.label('Var_value')
                )
                .join(SectionProperty, SectionValue.ng_sectionproperty == SectionProperty.id)
                .join(SectionVariable, SectionProperty.ng_idsectionvariable == SectionVariable.id)
                .join(Section, SectionValue.ng_section == Section.id)
                .join(SectionSeries, Section.pid == SectionSeries.id)
                .filter(SectionSeries.id.like(section_id))
             )
            res = sess.execute(query)
            df = pd.DataFrame(res.fetchall(), columns=res.keys())
            if df.empty:
                print("The query returned no results. Please check the input values or database data.")
            else:
                print(df)


