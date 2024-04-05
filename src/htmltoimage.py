# script to convert html to png
import pandas as pd 
import click
import subprocess


# grouping commands
@click.group()
def cli():
    pass

# cammand to convert html to png
@click.command()
@click.argument('template_path', type=click.Path(exists=True))
def convert(template_path):
    '''
    convert html to png output will be in current directory
    '''
    click.echo(f"converting {template_path} to output.png")
    subprocess.run(['wkhtmltoimage', template_path, 'C:/My-Files/Projects/certificate-creater/output/output.png'])

# cammand to convert html to png and save in specified location
@click.command()
@click.argument('template_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path(exists=True))
def convert_to_path(template_path, output_path):
    click.echo(f"converting {template_path} to {output_path}...")
    subprocess.run(['wkhtmltoimage', template_path, output_path])


# convert html to png with csv file as input and replace columns names with column names in csv
@click.command()
@click.argument('template_path', type=click.Path(exists=True))
@click.argument('csv_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path(exists=True))
def convert_csv(template_path, csv_path, output_path):

    df = pd.read_csv(csv_path)
    columns = df.columns
    for i in range(df.shape[0]):
        template_string = open(template_path).read()

        for s in columns:
            template_string = template_string.replace(f"[{s}]", str(df[s][i]))

        with open(output_path+'output.html', 'w') as f:
            f.write(template_string)

        subprocess.run(['wkhtmltoimage', output_path+'output.html', output_path+str(i)+'.png'])



cli.add_command(convert_csv)
cli.add_command(convert_to_path)
cli.add_command(convert)

if __name__ == '__main__':
    cli()