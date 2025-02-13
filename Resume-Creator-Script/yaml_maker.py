import yaml

# Your YAML template with placeholders
yaml_template = """
full name: {name}
job title: {job_title}
primary color: 008080
links:
  - Portfolio: {portfolio}
  - GitHub: {github}
  - LinkedIn: {linkedin}
  - {mail}: mailto:{mail}
  - "+91{phone}": tel:+91{phone}


not_links:
  - {city} | {country}

template: {template}


summary: |
  {summary}
  
skills:
  - {skill1}
  - {skill2}
  - {skill3}
  - {skill4}

experience:
  - {exp}:
    - {exp_dur}
    - |
      - {exp_work}

      Highlighted skills: {exp_skill}
  
projects:
  - {prj_name}:
      - |
        {prj_sum}

        Highlighted skills: {prj_skill}

education:
  - {degree}:
      - "{batch_year}"

  - {certi}:
      - "{certi_dur}"

"""

# Values to substitute
name = 'Bhuvi Ghate'
job_title='Developer'
portfolio = 'https://mowafy001.github.io/portfolio/'
github='https://github.com/MoWafy001'
linkedin='https://linkedin.com/in/mohamedwafy'
mail='wafy123445@gmail.com'
phone='8817896223'
city='Nagpur'
country='India'
template='Unnamed'
summary="""As a Fullstack Developer with 1 year of work experience, I bring expertise in both frontend and backend development, as well as Linux and cloud technologies.I am a hardworking and ambitious individual, with a passion for crafting high-quality code.My favorite programming languages include Typescript, Python, German, and Ruby.I am actively seeking new opportunities to contribute my skills and continue growing as a developer."""
skill1='s'
skill2='s'
skill3='s'
skill4='s'
prj_name='s'
prj_sum='s'
prj_skill='s'
degree='s'
batch_year='s'
exp='s'
exp_dur='s'
exp_work='s'
exp_skill='s'
degree='s'
batch_year='s'
certi='s'
certi_dur='s'

# Format the YAML with the provided values
formatted_yaml = yaml_template.format(name=name,job_title=job_title,portfolio=portfolio,github=github,linkedin=linkedin,mail=mail,phone=phone,city=city,country=country,template=template,summary=summary
                                      ,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,prj_name=prj_name,prj_sum=prj_sum,
                                      prj_skill=prj_skill,degree=degree,batch_year=batch_year,
exp=exp,
exp_dur=exp_dur,
exp_work=exp_work,
exp_skill=exp_skill,
certi=certi,
certi_dur=certi_dur)

# Write the formatted YAML to a file
with open('output.yaml', 'w') as file:
    file.write(formatted_yaml)