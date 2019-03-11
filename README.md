# ood-conf

Configurations for YCRC OOD deployments. Here we assume that the hosts in the inventory file `hosts` have been provisioned and have RHEL, Slurm, GPFS, already installed properly for the cluster that is to be served. We also expect [OpenOnDemand](http://openondemand.org) (ood) to be installed and ready to configure. Lots of other assumptions are made, so this will probably only work on our clusters (for now?).

## Ansible

Deployments are handled with Ansible. You need an ssh key authorized to log in as root on the ondemand nodes to deploy. Configuration files are either static or `jinja2` templated files all kept in the `config` directory. Please take a look at the playbook `ood-deploy.yml` for annotations and links to relevant ood documentation.

### Tags

Tasks in the playbook are [tagged](https://docs.ansible.com/ansible/latest/playbooks_tags.html) with categories. To just see a list, run `ansible-playbook --list-tags ood-deploy.yml`. The general idea is that you can either run all (and should when configuring a fresh install), or just redeploy the announcements, for example.

### To Deploy

To dry run:

``` bash
ansible-playbook --check --diff --connection=local -l ood.farnam ood-deploy.yml
```

To deploy:

``` bash
# to just farnam
ansible-playbook -l ood.farnam ood-deploy.yml
# to everyone
ansible-playbook ood-deploy.yml
```