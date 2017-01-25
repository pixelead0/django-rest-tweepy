# -*- coding: utf-8 -*-
"""
    Author  :   Adan GQ <adangq@gmail.com>
"""

from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator

class Customer(models.Model):
    """Model for Customers """
    name = models.CharField('Empresa', max_length=100, blank=False, null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['name']

    def __str__(self):
        return self.name


class Board(models.Model):
    """Model for Boards """
    name = models.CharField('Módulo', max_length=100, blank=False, null=False, unique=True)
    index_max = models.PositiveIntegerField('Indice Máximo', null=False)
    index_sync =models.PositiveIntegerField('Resincronización', null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['name']

    def __str__(self):
        return self.name


class Command(models.Model):
    """Model for Command """
    board = models.ForeignKey(Board, null=False)
    command = models.PositiveIntegerField('Num de Comando', blank=False, null=False)
    name = models.CharField('Nombre Comando', max_length=100, blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comando'
        verbose_name_plural = 'Comandos'
        ordering = ['board','command']
        unique_together = ('board', 'command')

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    """Model for Vehicle """
    board = models.ForeignKey(Board, null=False)
    customer = models.ForeignKey(Customer, null=False)
    name = models.CharField('Placa o Num Eco', max_length=100, blank=False, null=False)
    nip = models.PositiveIntegerField('NIP', blank=False, null=False)
    mask = models.PositiveIntegerField('Num Lote', blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering = ['board','customer', 'name']
        unique_together = ('board', 'customer', 'name')

    def __str__(self):
        return self.name
