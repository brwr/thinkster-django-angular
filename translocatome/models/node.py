from django.db import models


class Node(models.Model):
    uni_prot_ac = models.CharField(max_length=50)
    gene_name = models.CharField(max_length=50)
    base_activity = models.FloatField(null=True)
    base_concentration = models.FloatField(null=True)
    cancer_driver = models.FloatField(null=True)
    cancer_indirect_driver = models.FloatField(null=True)

    def natural_key(self):
        return self.id, self.uni_prot_ac, self.gene_name

    def __str__(self):
        return 'Node:uni_prot_ac<{uni_prot_ac}>, gene_name<{gene_name}>'.format(uni_prot_ac=self.uni_prot_ac, gene_name=self.gene_name)

    class Meta:
        unique_together = ('uni_prot_ac', 'gene_name',)
